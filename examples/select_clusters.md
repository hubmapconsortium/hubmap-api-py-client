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
>>> gene_symbol = client.select_genes().get_list()[0]['gene_symbol']
>>> clusters_with_gene_set = client.select_clusters(where='gene', has=[gene_symbol], genomic_modality='rna', p_value=0.05)
>>> assert len(clusters_with_gene_set) > 0
>>> clusters_with_gene_set.get_list()[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset'])

>>> cluster_keys = clusters_with_gene_set.get_list(values_included=[gene_symbol])[0]['values'].keys()
>>> assert list(cluster_keys) == [gene_symbol]

```

`client.select_clusters(where='dataset', ...)`:
```python
>>> dataset_uuid = client.select_datasets().get_list()[2]['uuid']
>>> clusters_in_dataset = client.select_clusters(where='dataset', has=[dataset_uuid])
>>> assert len(clusters_in_dataset) > 0

```
