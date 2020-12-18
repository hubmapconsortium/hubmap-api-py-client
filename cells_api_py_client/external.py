from cells_api_py_client.internal import InternalClient

_default_limit = 1000
_default_p_value = -1


class ExternalClient():
    def __init__(self, base_url):
        self.client = InternalClient(base_url)

    def _query(
            self,
            input_type, output_type, input_set,
            genomic_modality=None, limit=None, p_value=None):
        handle = self.client.hubmap_query(
            input_type, output_type, input_set,
            genomic_modality, limit, p_value)
        return ResultsSet(
            self.client, handle,
            input_type=input_type, output_type=output_type,
            input_set=input_set)


def _add_method(input_type):
    method_name = f'query_{input_type}s'
    method = (
        lambda self, output_type, input_set,
        genomic_modality=None, limit=_default_limit, p_value=_default_p_value:
        self._query(
            input_type, output_type, input_set,
            genomic_modality=genomic_modality, limit=limit, p_value=p_value)
    )
    setattr(ExternalClient, method_name, method)


for input_type in ['cell', 'organ', 'gene', 'cluster', 'protein', 'dataset']:
    _add_method(input_type)


class ResultsSet():
    def __init__(
            self, client, handle,
            input_type=None, output_type=None,
            input_set=None):
        self.client = client
        self.handle = handle
        self.input_type = input_type
        self.output_type = output_type
        self.input_set = input_set

    def __len__(self):
        return self.client.set_count(self.handle, self.output_type)

    # TODO: There may be bugs with union and intersection, perhaps on the server side?

    def __or__(self, other_set):
        new_handle = self.client.set_union(self.handle, other_set.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            input_set=self.input_set)

    def __and__(self, other_set):
        new_handle = self.client.set_intersection(self.handle, other_set.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            input_set=self.input_set)

    def __invert__(self):
        new_handle = self.client.set_negation(self.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            input_set=self.input_set)

    def __sub__(self, other_set):
        return self & ~ other_set

    def get_list(self, limit):
        return self.client.set_list_evaluation(self.handle, self.output_type, limit)

    def get_details(
            self, limit,
            values_included=[], sort_by=None):
        return self.client.set_detail_evaluation(
            self.handle, self.output_type, limit,
            sort_by=sort_by,
            values_type=self.input_type,
            values_included=self.input_set)
