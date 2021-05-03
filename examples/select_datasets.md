`client.select_datasets()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_datasets = client.select_datasets()
>>> assert len(all_datasets) > 0

```

`client.select_datasets(where='cell', )`:
```python
>>> from hubmap_cell_id_gen_py import get_sequencing_cell_id
>>> sequencing_cell_id = get_sequencing_cell_id('210d118a14c8624b6bb9610a9062656e','AAACAACGAAACGTGG')
>>> cell_datasets = client.select_datasets(where='cell', has=[sequencing_cell_id])
>>> assert len(cell_datasets) > 0

```

`client.select_datasets(where='cluster', ...)`:
```python
>>> cluster_datasets = client.select_datasets(where='cluster', has=['leiden-UMAP-1ca63edfa35971f475c91d92f4a70cb0-0'])
>>> assert len(cluster_datasets) > 0

```

`client.select_datasets(where='gene', ...)`:
```python
>>> gene_datasets = client.select_datasets(where='gene', has=['VIM > 1'], genomic_modality='rna', min_cell_percentage=10.0)
>>> assert len(cluster_datasets) > 0

```

`client.select_datasets(where='protein', ...)`:
```python
>>> protein_datasets = client.select_datasets(where='protein', has=['Ki67 > 10000'], min_cell_percentage=10.0)
>>> assert len(protein_datasets) > 0
