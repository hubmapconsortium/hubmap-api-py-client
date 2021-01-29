`client.select_proteins()`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> all_proteins = client.select_proteins()
>>> assert len(all_proteins) > 0

```

