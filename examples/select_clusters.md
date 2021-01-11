`client.select_clusters(where='gene', ...)`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> clusters_with_gene = client.select_clusters(where='gene', has=['CASTOR2'])
>>> assert len(clusters_with_gene) > 0

>>> clusters_with_gene[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset'])

>>> clusters_with_gene.get_details(1)[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset', 'values'])

```