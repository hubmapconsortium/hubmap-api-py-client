`client.select_organs()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_organs = client.select_organs()
>>> assert len(all_organs) > 0

```

`client.select_organs(where='gene', ...)`:
```python
>>> gene_symbol = client.select_genes().get_list()[10]['gene_symbol']
>>> organs_with_gene = client.select_organs(where='gene', has=[gene_symbol], genomic_modality='atac', p_value=0.05)
>>> assert len(organs_with_gene) > 0

>>> gene_keys = organs_with_gene.get_list(values_included=[gene_symbol])[0]['values'].keys()
>>> assert list(gene_keys) == [gene_symbol]

```

`client.select_organs(where='cell', ...)`:
```python
>>> cell_id = client.select_cells().get_list()[0]['cell_id']
>>> organs_with_cell = client.select_organs(where='cell', has=[cell_id])
>>> assert len(organs_with_cell) > 0

```