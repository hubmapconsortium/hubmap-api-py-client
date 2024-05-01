`client.select_proteins()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_proteins = client.select_proteins()
>>> assert len(all_proteins) > 0

```

No other protein queries currently supported.
