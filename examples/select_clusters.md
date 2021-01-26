`client.select_clusters(where='gene', ...)`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> clusters_with_gene = client.select_clusters(where='gene', has=['CASTOR2'], genomic_modality='atac', p_value=0.05)
>>> assert len(clusters_with_gene) > 0

>>> clusters_with_gene[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset'])

>>> clusters_with_gene.get_details(1)[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset', 'values'])

```

`client.select_clusters(where='dataset', ...)`:
```python

>>> clusters_in_dataset = client.select_clusters(where='dataset', has=['d4493657cde29702c5ed73932da5317c'])
>>> assert len(clusters_in_dataset) > 0

```