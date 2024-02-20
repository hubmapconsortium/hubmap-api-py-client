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
>>> cell_id = client.select_cells().get_list()[0]['cell_id']
>>> cell_datasets = client.select_datasets(where='cell', has=[cell_id])
>>> assert len(cell_datasets) > 0

```

`client.select_datasets(where='cluster', ...)`:
```python
>>> dataset = client.select_datasets().get_list()[0]['uuid']
>>> cluster_name = client.select_clusters(where='dataset', has=[dataset]).get_list()[0]['grouping_name']
>>> cluster_datasets = client.select_datasets(where='cluster', has=[cluster_name])
>>> assert len(cluster_datasets) > 0

```

`client.select_datasets(where='gene', ...)`:
```python
>>> gene_symbol = client.select_genes(where="modality",has=["rna"]).get_list()[0]['gene_symbol']
>>> gene_datasets = client.select_datasets(where='gene', has=[f'{gene_symbol} > 1'], genomic_modality='rna', min_cell_percentage=0.0)
>>> assert len(gene_datasets) > 0

```

`client.select_datasets(where='protein', ...)`:
```python
>>> protein_name = client.select_proteins().get_list()[0]['protein_id']
>>> protein_datasets = client.select_datasets(where='protein', has=[f'{protein_name} > 1000'], min_cell_percentage=5.0)
>>> assert len(protein_datasets) > 0

```

`client.select_cells(where='modality', ...)`:
```python
>>> datasets_in_modality = client.select_datasets(where='modality', has=['rna'])
>>> assert len(datasets_in_modality) > 0

```

`client.select_datasets(where='celltype', ...)`:
```python
>>> cell_type = client.select_celltypes().get_list()[0]['grouping_name']
>>> datasets_with_celltype = client.select_datasets(where='celltype', has=[cell_type])
>>> assert len(datasets_with_celltype) > 0

```