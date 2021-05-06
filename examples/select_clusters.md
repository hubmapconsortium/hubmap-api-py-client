`client.select_clusters()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_clusters = client.select_clusters()
>>> assert len(all_clusters) > 0

```

`client.select_clusters(where='gene', ...)`:
```python
>>> clusters_with_gene_set = client.select_clusters(where='gene', has=['CASTOR2'], genomic_modality='rna', p_value=0.05)
>>> assert len(clusters_with_gene_set) > 0
>>> clusters_with_gene_set.get_list()[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset'])

>>> clusters_with_gene_set.get_list(values_included=['CASTOR2'])[0]['values'].keys()
dict_keys(['CASTOR2'])

```

`client.select_clusters(where='dataset', ...)`:
```python
>>> clusters_in_dataset = client.select_clusters(where='dataset', has=['d4493657cde29702c5ed73932da5317c'])
>>> assert len(clusters_in_dataset) > 0

```
