from typing import List

import requests

HANDLE = 'query_handle'


class ApiError(Exception):
    pass


class InternalClient():
    def __init__(self, base_url):
        # 'https://cells.dev.hubmapconsortium.org/api/'
        self.base_url = base_url

    def _check_parameters(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str, p_value: float):
        output_types = ['cell', 'organ', 'gene', 'cluster', 'dataset', 'protein']
        if output_type not in output_types:
            raise ValueError(f'{output_type} not in {output_types}')

        input_types = {
            # Allowed input types vary depending on output type
            'cell': ['cell', 'gene', 'organ', 'protein', 'dataset'],
            'organ': ['organ', 'cell', 'gene'],
            'gene': ['gene', 'organ', 'cluster'],
            'cluster': ['cluster', 'gene', 'dataset'],
            'dataset': ['dataset', 'cell', 'cluster'],
            'protein': [],  # Only allow queries for all proteins
        }
        if input_type not in input_types[output_type]:
            raise ValueError(f'{input_type} not in {input_types[output_type]}')

    def _fill_request_dict(
            self,
            input_type: str, input_set: List[str],
            genomic_modality: str, p_value: float, logical_operator: str):

        params = {'genomic_modality': genomic_modality, 'p_value': p_value,
                  'logical_operator': logical_operator}
        request_dict = {param_name: params[param_name] for param_name in params
                        if params[param_name] is not None}
        request_dict['input_type'] = input_type
        request_dict['input_set'] = input_set

        return request_dict

    def hubmap_query(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str = None, p_value: float = None, logical_operator: str = None):
        '''
        This function takes query parameters and returns a query set token.
        '''
        request_url = self.base_url + output_type + "/"
        if input_type is None:
            # TODO: Is this really needed? Could we just send an empty POST?
            response = requests.get(request_url)
        else:
            self._check_parameters(
                input_type=input_type, output_type=output_type,
                input_set=input_set, genomic_modality=genomic_modality, p_value=p_value)
            request_dict = self._fill_request_dict(
                input_type, input_set, genomic_modality, p_value, logical_operator)
            response = requests.post(request_url, request_dict)
        return self._handle_from_response(response)

    def _handle_from_response(self, response):
        response_json = response.json()
        if 'results' not in response_json:
            raise ApiError() # TODO: Return human readable message, not stack trace
        # Returns the key to be used in future computations
        return response_json['results'][0][HANDLE]

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
        request_dict = {"key_one": set_key_one, "key_two": set_key_two, "set_type": set_type}
        response = requests.post(request_url, request_dict)
        return self._handle_from_response(response)

    # These functions take a query set token and return an evaluated query_set:

    def _check_detail_parameters(
            self, set_type, values_type):
        type_map = {'cell': ['gene', 'protein'], 'gene': [
            'organ', 'cluster'], 'cluster': ['gene'], 'organ': ['gene']}
        allowed_types = type_map[set_type]
        if values_type not in allowed_types:
            raise ValueError(
                f'For "{set_type}", only {allowed_types} allowed, not "{values_type}"')

    def set_count(
            self, set_key: str, set_type: str) -> str:
        request_url = self.base_url + "count/"
        request_dict = {"key": set_key, "set_type": set_type}
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        return results[0]["count"]

    def set_list_evaluation(
            self, set_key: str, set_type: str, limit: int, offset: int = 0):
        '''
        This function/API call returns a minimal version of the set,
        containing a list of cells/genes/etc w/o
        associated quantitative values.  It should be reasonably fast.
        '''
        request_url = self.base_url + set_type + "evaluation/"
        request_dict = {"key": set_key, "set_type": set_type, "limit": limit, "offset": offset}
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        return results  # Returns the key to be used in future computations

    def set_detail_evaluation(
            self, set_key: str, set_type: str, limit: int,
            values_included: List = [], sort_by: str = None, values_type: str = None,
            offset: int = 0):
        '''
        This function/API call returns a more detailed version of the set,
        containing data specified in include_values
        It may be slow.
        '''
        self._check_detail_parameters(set_type, values_type)
        request_url = self.base_url + set_type + "detailevaluation/"
        request_dict = {"key": set_key, "set_type": set_type, "limit": limit, "offset": offset,
                        "values_included": values_included, "sort_by": sort_by,
                        "values_type": values_type}
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        return results  # Returns the key to be used in future computations
