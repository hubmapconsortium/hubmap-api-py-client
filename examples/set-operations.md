Providing a list to `has` is the same as using `|` for the union:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> a_uuid = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> b_uuid = 'e8d642084fc5ec8b5d348ebab96a4b22'

>>> a_cells = client.select_cells(where='dataset', has=a_uuid)
>>> b_cells = client.select_cells(where='dataset', has=b_uuid)

>>> len_a_cells = len(a_cells)
>>> len_b_cells = len(b_cells)

>>> assert len_a_cells > 0
>>> assert len_b_cells > 0

>>> a_b_union_operator = \
...     client.select_cells(where='dataset', has=a_uuid) \
...     | client.select_cells(where='dataset', has=b_uuid)
>>> a_b_union_query = \
...     client.select_cells(where='dataset', has=[a_uuid, b_uuid])

>>> assert len(a_b_union_query) == len(a_b_union_operator)
>>> assert len(a_b_union_query) == len_a_cells + len_b_cells

```