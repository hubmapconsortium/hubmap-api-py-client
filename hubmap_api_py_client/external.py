from hubmap_api_py_client.internal import InternalClient

_default_limit = 1000


class ExternalClient():
    def __init__(self, base_url):
        self.client = InternalClient(base_url)

    def __repr__(self):
        return f'<Client base_url={self.client.base_url}>'

    def _query(
            self,
            input_type=None, output_type=None, has=None,
            genomic_modality=None, limit=None, p_value=None,
            ResultsSetSubclass=None):
        if not isinstance(has, list):
            raise TypeError(f'"has" parameter must be a list, not {has}')
        handle = self.client.hubmap_query(
            input_type, output_type, has,
            genomic_modality, limit, p_value)
        return ResultsSetSubclass(
            self.client, handle,
            input_type=input_type, output_type=output_type,
            query=has
        )


def _add_method(output_type, ResultsSetSubclass):
    method_name = f'select_{output_type}s'
    method = (
        lambda self, where=None, has=None,
        genomic_modality=None, limit=_default_limit, p_value=None:
        self._query(
            input_type=where, output_type=output_type, has=has,
            genomic_modality=genomic_modality, limit=limit, p_value=p_value,
            ResultsSetSubclass=ResultsSetSubclass)
    )
    setattr(ExternalClient, method_name, method)


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

    def __repr__(self):
        return (
            f'<{class_name(self.output_type)} '
            f'base_url={self.client.base_url} handle={self.handle}>')

    def __len__(self):
        return self.client.set_count(self.handle, self.output_type)

    def __or__(self, other_set):
        return self._operation(other_set, self.client.set_union)

    def __and__(self, other_set):
        return self._operation(other_set, self.client.set_intersection)

    def __sub__(self, other_set):
        return self._operation(other_set, self.client.set_difference)

    def _operation(self, other_set, method):
        if self.output_type != other_set.output_type:
            raise ValueError(
                'Operand output types do not match: '
                f'{self.output_type} != {other_set.output_type}')
        new_handle = method(self.handle, other_set.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            query=self.query)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                raise ValueError('Negative index not supported')
            return self._get_list(1, offset=key)[0]
        if isinstance(key, slice):
            if key.step is not None:
                raise ValueError('Step is not supported')
            if key.start is None or key.stop is None:
                raise ValueError('Start and stop are required')
            if key.start < 0 or key.stop < 0:
                raise ValueError('Start and stop must be >= 0')
            if key.stop < key.start:
                raise ValueError('Stop must be > start')
            return self._get_list(key.stop - key.start, offset=key.start)
        raise TypeError()

    def _get_list(self, limit, offset=0):
        return self.client.set_list_evaluation(self.handle, self.output_type, limit, offset=offset)

    def get_details(
            self, limit, offset=0,
            values_included=[], sort_by=None):
        return self.client.set_detail_evaluation(
            self.handle, self.output_type, limit,
            offset=offset,
            sort_by=sort_by,
            values_type=self.input_type,
            values_included=[self.query])


def class_name(output_type):
    return f'{output_type.capitalize()}ResultsSet'


def _create_subclass(output_type):
    return type(class_name(output_type), (ResultsSet,), {})


for output_type in ['cell', 'organ', 'gene', 'cluster']:
    ResultsSetSubclass = _create_subclass(output_type)
    _add_method(output_type, ResultsSetSubclass)
