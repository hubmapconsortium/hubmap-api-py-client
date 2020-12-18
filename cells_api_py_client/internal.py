from typing import List

import requests

output_types = ['cell', 'organ', 'gene', 'cluster']
input_types = {
    # Allowed input types vary depending on output type
    'cell': ['gene', 'organ', 'protein', 'dataset'],
    'organ': ['cell', 'gene'],
    'gene': ['organ', 'cluster'],
    'cluster': ['gene']
}
genomic_modalities = ['rna', 'atac']  # Used for quantitative gene->cell queries

HANDLE = 'query_pickle_hash'


class InternalClient():
    def __init__(self, base_url):
        # 'https://cells.dev.hubmapconsortium.org/api/'
        self.base_url = base_url

    def _check_parameters(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str, p_value: float = 0.05):
        assert output_type in output_types
        assert input_type in input_types[output_type]
        if input_type == 'gene' and output_type == 'cell':
            assert genomic_modality in genomic_modalities
        if (input_type == 'organ' and output_type == 'gene'
                or input_type == 'gene' and output_type == 'organ'):
            assert p_value >= 0.0 and p_value <= 1.0

    def _fill_request_dict(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str, p_value: float):
        request_dict = {'input_type': input_type, 'input_set': input_set}
        if input_type == 'gene' and output_type == 'cell':
            request_dict['genomic_modality'] = genomic_modality
        if (input_type == 'organ' and output_type == 'gene'
                or input_type == 'gene' and output_type == 'organ'):
            request_dict['p_value'] = p_value
        if genomic_modality is not None:
            request_dict['genomic_modality'] = genomic_modality
        request_dict['logical_operator'] = "and"
        return request_dict

    def hubmap_query(
            self,
            input_type: str, output_type: str, input_set: List[str],
            genomic_modality: str = None, limit: int = 1000, p_value: float = -1.0):
        '''
        This function takes query parameters and returns a query set token.
        '''
        self._check_parameters(input_type, output_type, input_set, genomic_modality, p_value)
        request_url = self.base_url + output_type + "/"
        request_dict = self._fill_request_dict(
            input_type, output_type, input_set, genomic_modality, p_value)
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        # Returns the key to be used in future computations
        return results[0][HANDLE]

    # These functions take one or two query set tokens and return an API token

    def set_intersection(
            self, set_key_one: str, set_key_two: str, set_type: str) -> str:
        request_url = self.base_url + "intersection/"
        request_dict = {"key_one": set_key_one, "key_two": set_key_two, "set_type": set_type}
        results = requests.post(request_url, request_dict).json()['results']
        # Returns the key to be used in future computations
        return results[0][HANDLE]

    def set_union(
            self, set_key_one: str, set_key_two: str, set_type: str) -> str:
        request_url = self.base_url + "union/"
        request_dict = {"key_one": set_key_one, "key_two": set_key_two, "set_type": set_type}
        results = requests.post(request_url, request_dict).json()['results']
        # Returns the key to be used in future computations
        return results[0][HANDLE]

    def set_negation(
            self, set_key: str, set_type: str) -> str:
        request_url = self.base_url + "negation/"
        request_dict = {"key": set_key, "set_type": set_type}
        results = requests.post(request_url, request_dict).json()['results']
        # Returns the key to be used in future computations
        return results[0][HANDLE]

    # These functions/API calls take a query set token and return an evaluated query_set

    def _check_detail_parameters(
            self, set_type, values_type):
        type_map = {'cell': ['gene', 'protein'], 'gene': [
            'organ', 'cluster'], 'cluster': ['gene'], 'organ': ['gene']}
        allowed_types = type_map[set_type]
        if values_type not in allowed_types:
            raise Exception(f'For "{set_type}", only {allowed_types} allowed, not "{values_type}"')

    def set_count(
            self, set_key: str, set_type: str) -> str:
        request_url = self.base_url + "count/"
        request_dict = {"key": set_key, "set_type": set_type}
        results = requests.post(request_url, request_dict).json()['results']
        return results[0]["count"]

    def set_list_evaluation(
            self, set_key: str, set_type: str, limit: int):
        '''
        This function/API call returns a minimal version of the set,
        containing a list of cells/genes/etc w/o
        associated quantitative values.  It should be reasonably fast.
        '''
        request_url = self.base_url + set_type + "evaluation/"
        request_dict = {"key": set_key, "set_type": set_type, "limit": limit}
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        return results  # Returns the key to be used in future computations

    def set_detail_evaluation(
            self, set_key: str, set_type: str, limit: int,
            values_included: List = [], sort_by: str = None, values_type: str = None):
        '''
        This function/API call returns a more detailed version of the set,
        containing data specified in include_values
        It may be slow.
        '''
        self._check_detail_parameters(set_type, values_type)
        request_url = self.base_url + set_type + "detailevaluation/"
        request_dict = {"key": set_key, "set_type": set_type, "limit": limit,
                        "values_included": values_included, "sort_by": sort_by,
                        "values_type": values_type}
        response = requests.post(request_url, request_dict)
        results = response.json()['results']
        return results  # Returns the key to be used in future computations