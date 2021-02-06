`client.select_datasets(where='cell', )`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')
>>> from hubmap_cell_id_gen_py import get_sequencing_cell_id
>>> sequencing_cell_id = get_sequencing_cell_id('210d118a14c8624b6bb9610a9062656e','AAACAACGAAACGTGG')
>>> cell_datasets = client.select_datasets(where='cell', has=[sequencing_cell_id])
>>> assert len(cell_datasets) > 0

```

`client.select_datasets(where='cluster', ...)`:
```python
>>> cluster_datasets = client.select_datasets(where='cluster', has=['d4493657cde29702c5ed73932da5317c-19'])
>>> assert len(cluster_datasets) > 0

```
