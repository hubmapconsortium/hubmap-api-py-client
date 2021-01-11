```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')
>>> client
<Client base_url=https://cells.dev.hubmapconsortium.org/api/>

>>> cells_with_vim = client.select_cells(where='gene', has=['VIM > 0.5'], genomic_modality='rna')
>>> type(cells_with_vim)
<class 'hubmap_api_py_client.external.CellResultsSet'>

>>> import re
>>> re.sub(r'=[^ >]+', '=...', str(cells_with_vim))
'<CellResultsSet base_url=... handle=...>'

```
