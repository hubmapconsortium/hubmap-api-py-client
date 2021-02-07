`client.select_proteins()`:
```python
>>> from hubmap_api_py_client import Client, test_url
>>> client = Client(test_url)

>>> all_proteins = client.select_proteins()
>>> assert len(all_proteins) > 0

```

No other protein queries currently supported.
