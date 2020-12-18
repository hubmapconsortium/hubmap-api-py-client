from cells_api_py_client.internal import InternalClient


class ExternalClient():
    def __init__(self, base_url):
        self.client = InternalClient(base_url)

    def query(
            self,
            input_type, output_type, input_set,
            genomic_modality=None, limit=1000, p_value=-1.0):
        handle = self.client.hubmap_query(
            input_type, output_type, input_set,
            genomic_modality, limit, p_value)
        return ResultsSet(self.client, handle, output_type)


class ResultsSet():
    def __init__(self, client, handle, set_type):
        self.client = client
        self.handle = handle
        self.set_type = set_type

    def __len__(self):
        return self.client.set_count(self.handle, self.set_type)

    def __or__(self, other_set):
        new_handle = self.client.set_union(self.handle, other_set.handle, self.set_type)
        return ResultsSet(self.client, new_handle, self.set_type)

    def __and__(self, other_set):
        new_handle = self.client.set_intersection(self.handle, other_set.handle, self.set_type)
        return ResultsSet(self.client, new_handle, self.set_type)

    def get_list(self, limit):
        return self.client.set_list_evaluation(self.handle, self.set_type, limit)

    def get_details(
            self, limit,
            values_included=[], sort_by=None, values_type=None):
        return self.client.set_detail_evaluation(
            self.handle, self.set_type, limit,
            values_included=values_included,
            sort_by=sort_by,
            values_type=values_type)
