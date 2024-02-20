`client.select_celltypes()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_celltypes = client.select_celltypes()
>>> assert len(all_celltypes) > 0

```

`client.select_celltypes(where='celltype', )`:
```python
>>> celltype_name = client.select_celltypes().get_list()[0]['grouping_name']
>>> celltypes = client.select_celltypes(where='celltype', has=[celltype_name])
>>> assert len(celltypes) > 0

```

`client.select_celltypes(where='cell', )`:
```python
>>> cell_type = client.select_celltypes().get_list()[0]['grouping_name']
>>> cell_id = client.select_cells(where="celltype", has=[cell_type]).get_list()[0]['cell_id']
>>> cell_celltypes = client.select_celltypes(where='cell', has=[cell_id])
>>> assert len(cell_celltypes) >= 0

```


`client.select_celltypes(where='dataset', )`:
```python
>>> cell_type = client.select_celltypes().get_list()[0]['grouping_name']
>>> uuid = client.select_datasets(where="celltype",has=[cell_type]).get_list()[0]['uuid']
>>> dataset_celltypes = client.select_celltypes(where='dataset', has=[uuid])
>>> assert len(cell_celltypes) > 0

```

`client.select_celltypes(where='organ', )`:
```python
>>> cell_type = client.select_celltypes().get_list()[0]['grouping_name']
>>> organ_name = client.select_organs(where="celltype", has=[cell_type]).get_list()[0]['grouping_name']
>>> organ_celltypes = client.select_celltypes(where='organ', has=[organ_name])
>>> assert len(cell_celltypes) > 0

```
