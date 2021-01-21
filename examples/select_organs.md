`client.select_organs(where='gene')`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_gene = client.select_organs(where='gene', has=['CHN2'], genomic_modality='atac')
>>> assert len(organs_with_gene) > 0
```

`client.select_organs(where='cell', ...)`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_gene = client.select_organs(where='cell', has=['CHN2'])
>>> assert len(organs_with_gene) > 0```