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
>>> li_genes = client.select_genes(where='organ', has=['Large Intestine'], genomic_modality='rna', p_value=0.05)

>>> li_genes_details = li_genes.get_list()
>>> li_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

>>> li_genes_details_with_values = li_genes.get_list(values_included=['Large Intestine'])
>>> li_genes_details_with_values[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'values'])

>>> li_genes_details_with_values[0]['values'].keys()
dict_keys(['Large Intestine'])

```

`client.select_genes(where='cluster', ...)`:
```python
TODO
```
Not sure what `has` value would work. [Filed issue](https://github.com/hubmapconsortium/hubmap-api-py-client/issues/16)