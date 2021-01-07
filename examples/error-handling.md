```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> client.select_cells(where='fake', has=['VIM>1'], genomic_modality='rna')
Traceback (most recent call last):
...
cells_api_py_client.internal.ClientException: fake not in ['gene', 'organ', 'protein', 'dataset']

>>> client.select_cells(where='gene', has=['VIM>1'], genomic_modality='fake')
Traceback (most recent call last):
...
cells_api_py_client.internal.ClientException: fake not in ['rna', 'atac']

```

Not clear why `atac` can't be used; [issue filed](https://github.com/hubmapconsortium/cells-api-py-client/issues/8).
```python
>>> client.select_cells(where='gene', has=['VIM>1'], genomic_modality='atac')
Traceback (most recent call last):
...
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

```