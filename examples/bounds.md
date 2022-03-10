

```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> rna_bounds = client.get_bounds('rna')
>>> atac_bounds = client.get_bounds('atac')
>>> codex_bounds = client.get_bounds('codex')

>>> rna_bounds.keys()
dict_keys(['minimum_value', 'maximum_value'])

>>> max_rna_value = rna_bounds['maximum_value']
>>> max_atac_value = atac_bounds['maximum_value']
>>> max_codex_value = codex_bounds['maximum_value']

>>> min_rna_value = rna_bounds['minimum_value']
>>> min_atac_value = atac_bounds['minimum_value']
>>> min_codex_value = codex_bounds['minimum_value']


>>> assert max_codex_value > min_codex_value and max_rna_value > min_rna_value and max_atac_value > min_atac_value

```