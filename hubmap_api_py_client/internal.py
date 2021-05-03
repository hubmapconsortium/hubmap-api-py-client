from typing import List

import requests

from hubmap_api_py_client.errors import ClientError

HANDLE = 'query_handle'


class InternalClient():
    def __init__(self, base_url):
        self.base_url = base_url

    def hubmap_query(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str = None, p_value: float = None, logical_operator: str = None,
            min_cell_percentage: float = None):
        '''
        This function takes query parameters and returns a query set token.
        '''
        request_url = self.base_url + output_type + "/"
        request_dict = {
            'input_type': input_type,
            'input_set': input_set,
            'genomic_modality': genomic_modality,
            'p_value': p_value,
            'logical_operator': logical_operator,
            'min_cell_percentage': min_cell_percentage
        }
        return self._post_and_get_handle(request_url, request_dict)

    # These functions take two query set tokens and return an API token:

    def set_intersection(
            self, set_key_one: str, set_key_two: str, set_type: str) -> str:
        return self._operation(set_key_one, set_key_two, set_type, 'intersection/')

    def set_union(
            self, set_key_one: str, set_key_two: str, set_type: str) -> str:
        return self._operation(set_key_one, set_key_two, set_type, 'union/')

    def set_difference(
            self, set_key_one: str, set_key_two: str, set_type: str) -> str:
        return self._operation(set_key_one, set_key_two, set_type, 'difference/')

    def _operation(
            self, set_key_one: str, set_key_two: str, set_type: str, path: str) -> str:
        request_url = self.base_url + path
        request_dict = {
            "key_one": set_key_one,
            "key_two": set_key_two,
            "set_type": set_type
        }
        return self._post_and_get_handle(request_url, request_dict)

    # These functions take a query set token and return an evaluated query_set:

    def set_count(
            self, set_key: str, set_type: str) -> str:
        request_url = self.base_url + "count/"
        request_dict = {"key": set_key, "set_type": set_type}
        results = self._post_and_get_results(request_url, request_dict)
        return results[0]["count"]

    def set_list_evaluation(
            self, set_key: str, set_type: str, limit: int, offset: int = 0):
        '''
        This function/API call returns a minimal version of the set,
        containing a list of cells/genes/etc w/o
        associated quantitative values.  It should be reasonably fast.
        '''
        request_url = self.base_url + set_type + "evaluation/"
        request_dict = {
            "key": set_key,
            "set_type": set_type,
            "limit": limit,
            "offset": offset
        }
        return self._post_and_get_results(request_url, request_dict)

    def set_detail_evaluation(
            self, set_key: str, set_type: str, limit: int,
            values_included: List = [], sort_by: str = None,
            offset: int = 0):
        '''
        This function/API call returns a more detailed version of the set,
        containing data specified in include_values
        It may be slow.
        '''
        request_url = self.base_url + set_type + "detailevaluation/"
        request_dict = {
            "key": set_key,
            "set_type": set_type,
            "limit": limit,
            "offset": offset,
            "values_included": values_included,
            "sort_by": sort_by
        }
        return self._post_and_get_results(request_url, request_dict)

    def _post_and_get_results(self, url, request_dict):
        response = requests.post(url, request_dict)
        response_json = response.json()
        if 'results' not in response_json:
            raise ClientError(response_json['message'])
        return response_json['results']

    def _post_and_get_handle(self, url, request_dict):
        response = self._post_and_get_results(url, request_dict)
        return response[0][HANDLE]
