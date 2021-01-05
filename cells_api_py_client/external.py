from cells_api_py_client.internal import InternalClient

_default_limit = 1000
_default_p_value = -1


class ExternalClient():
    def __init__(self, base_url):
        self.client = InternalClient(base_url)

    def _query(
            self,
            input_type=None, output_type=None, query=None,
            genomic_modality=None, limit=None, p_value=None):
        handle = self.client.hubmap_query(
            input_type, output_type, query,
            # TODO: input_set is currently reading only the last in the list.
            # https://github.com/hubmapconsortium/cells-api-py-client/issues/4
            genomic_modality, limit, p_value)
        return ResultsSet(
            self.client, handle,
            input_type=input_type, output_type=output_type,
            query=query
        )


def _add_method(output_type):
    method_name = f'select_{output_type}s'
    method = (
        lambda self, where=None, has=None,
        genomic_modality=None, limit=_default_limit, p_value=_default_p_value:
        self._query(
            input_type=where, output_type=output_type, query=has,
            genomic_modality=genomic_modality, limit=limit, p_value=p_value)
    )
    setattr(ExternalClient, method_name, method)


for output_type in ['cell', 'organ', 'gene', 'cluster']:
    _add_method(output_type)


class ResultsSet():
    def __init__(
            self, client, handle,
            input_type=None, output_type=None,
            query=None):
        self.client = client
        self.handle = handle
        self.input_type = input_type
        self.output_type = output_type
        self.query = query

    def __len__(self):
        return self.client.set_count(self.handle, self.output_type)

    def __or__(self, other_set):
        return self._operation(other_set, self.client.set_union)

    def __and__(self, other_set):
        return self._operation(other_set, self.client.set_intersection)

    def __sub__(self, other_set):
        return self._operation(other_set, self.client.set_difference)

    def _operation(self, other_set, method):
        new_handle = method(self.handle, other_set.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            query=self.query)

    def get_list(self, limit):
        return self.client.set_list_evaluation(self.handle, self.output_type, limit)

    def get_details(
            self, limit,
            values_included=[], sort_by=None):
        return self.client.set_detail_evaluation(
            self.handle, self.output_type, limit,
            sort_by=sort_by,
            values_type=self.input_type,
            values_included=[self.query])
