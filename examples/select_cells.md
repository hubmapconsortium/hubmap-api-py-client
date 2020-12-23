`client.select_cells(where='gene', ...)`:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> cells_with_gene = client.select_cells(where='gene', has='CASTOR2 > 1', genomic_modality='rna')
>>> assert len(cells_with_gene) > 0

```

`client.select_cells(where='organ', ...)`:
```python
>>> cells_in_kidney = client.select_cells(where='organ', has='Kidney')
>>> assert len(cells_in_kidney) > 0

```

`client.select_cells(where='protein', ...)`:
```python
TODO

```
[Filed issue](https://github.com/hubmapconsortium/cells-api-py-client/issues/17)

`client.select_cells(where='dataset', ...)`:
```python
>>> cells_in_dataset = client.select_cells(where='dataset', has='68159e4bd6a2cea1cd66e8f3050cfcb7')
>>> assert len(cells_in_dataset) > 0

```