`client.select_genes()`:
```python
>>> from hubmap_api_py_client import Client, test_url
>>> client = Client(test_url)

>>> all_genes = client.select_genes()
>>> assert len(all_genes) > 0

```

`client.select_genes(where='organ', ...)`:
```python
>>> kidney_genes = client.select_genes(where='organ', has=['Kidney'], genomic_modality='rna', p_value=0.05)

>>> kidney_genes_details = kidney_genes.get_list()
>>> kidney_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

>>> kidney_genes_details_with_values = kidney_genes.get_list(values_included=['Kidney'])
>>> kidney_genes_details_with_values[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'values'])

>>> kidney_genes_details_with_values[0]['values'].keys()
dict_keys(['Kidney'])

```

`client.select_genes(where='cluster', ...)`:
```python
TODO
```
Not sure what `has` value would work. [Filed issue](https://github.com/hubmapconsortium/hubmap-api-py-client/issues/16)