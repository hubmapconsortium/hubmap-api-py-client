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
>>> gene_symbol = client.select_genes(where="modality", has=["rna"]).get_list()[0]['gene_symbol']
>>> organs_with_gene = client.select_organs(where='gene', has=[gene_symbol], genomic_modality='rna', p_value=1.0)
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

`client.select_organs(where='celltype', ...)`:
```python
>>> cell_type = client.select_celltypes().get_list()[0]['grouping_name']
>>> organs_with_celltype = client.select_organs(where='celltype', has=[cell_type])
>>> assert len(organs_with_cell) > 0

```