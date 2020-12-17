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
        return ResultsSet(self.client, handle)


class ResultsSet():
    def __init__(self, client, handle):
        self.client = client
        self.handle = handle

    def get_count(self, set_type):
        return self.client.set_count(self.handle, set_type)

    def get_list(self, set_type, limit):
        return self.client.set_list_evaluation(self.handle, set_type, limit)

    def get_details(
            self, set_type, limit,
            values_included=[], sort_by=None, values_type=None):
        return self.client.set_detail_evaluation(
            self.handle, set_type, limit,
            values_included, sort_by, values_type)
