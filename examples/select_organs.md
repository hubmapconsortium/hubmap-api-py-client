`client.select_organs(where='gene')`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_gene = client.select_organs(where='gene', has=['CHN2'], genomic_modality='atac', p_value=0.05)
>>> assert len(organs_with_gene) > 0

```

`client.select_organs(where='cell', ...)`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_gene = client.select_organs(where='cell', has=['210d118a14c8624b6bb9610a9062656e-AAACAACGAAACGTGG'])
>>> assert len(organs_with_gene) > 0

```