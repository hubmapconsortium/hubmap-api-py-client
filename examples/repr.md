```python
>>> import re
>>> def abbreviate(s):
...     return re.sub(r'=[^ <>]+', r'=...', str(s))

>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])
>>> client
<Client base_url=https://cells.api.hubmapconsortium.org/api/>

>>> cells_set = client.select_cells(where='gene', has=['VIM > 0.5'], genomic_modality='rna')
>>> type(cells_set)
<class 'hubmap_api_py_client.external.CellResultsSet'>

>>> abbreviate(cells_set)
'<CellResultsSet base_url=... handle=...>'

>>> cells_list = cells_set.get_list()
>>> type(cells_list)
<class 'hubmap_api_py_client.external.ResultsList'>

>>> abbreviate(cells_list)
'<ResultsList results_set=<CellResultsSet base_url=... handle=...> values_included=... sort_by=...>'

```
