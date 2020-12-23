`client.select_genes(where='organ', ...)`:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> kidney_genes = client.select_genes(where='organ', has='Kidney', genomic_modality='rna', p_value=0.05)
>>> kidney_genes.get_list(10)[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

>>> kidney_genes_details = kidney_genes.get_details(10)
>>> kidney_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'values'])

>>> kidney_genes_details[0]['values'].keys()
dict_keys(['Kidney'])

```

`client.select_genes(where='cluster', ...)`:
```python
TODO
```
Not sure what `has` value would work. [Filed issue](https://github.com/hubmapconsortium/cells-api-py-client/issues/16)