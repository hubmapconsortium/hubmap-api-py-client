`client.select_clusters(where='gene', ...)`:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> clusters_with_gene = client.select_clusters(where='gene', has='CASTOR2')

```