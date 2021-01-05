`client.select_clusters(where='gene', ...)`:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> clusters_with_gene = client.select_clusters(where='gene', has='CASTOR2')
>>> assert len(clusters_with_gene) > 0

>>> clusters_with_gene.get_list(1)[0].keys()
dict_keys(['cluster_method', 'cluster_data', 'grouping_name', 'dataset'])

```

Expecting more keys here. [Filed issue](https://github.com/hubmapconsortium/cells-api-py-client/issues/22).
```python
>>> clusters_with_gene.get_details(1)[0].keys()
dict_keys(['grouping_name', 'dataset', 'values'])

```