`client.select_genes()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_genes = client.select_genes()
>>> assert len(all_genes) > 0

```

`client.select_genes(where='organ', ...)`:
```python
>>> organ_name = client.select_organs().get_list()[1]['grouping_name']
>>> organ_genes = client.select_genes(where='organ', has=[organ_name], genomic_modality='rna', p_value=0.05)

>>> organ_genes_details = organ_genes.get_list()
>>> organ_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

>>> organ_genes_details_with_values = organ_genes.get_list(values_included=[organ_name])
>>> organ_genes_details_with_values[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'values'])

>>> organ_keys = organ_genes_details_with_values[0]['values'].keys()
>>> assert list(organ_keys) == [organ_name]

```

`client.select_genes(where='cluster', ...)`:
```python
TODO
```
Not sure what `has` value would work. [Filed issue](https://github.com/hubmapconsortium/hubmap-api-py-client/issues/16)