`client.select_organs()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_organs = client.select_organs()
>>> assert len(all_organs) > 0

```

`client.select_organs(where='gene', ...)`:
```python
>>> organs_with_gene = client.select_organs(where='gene', has=['CHN2'], genomic_modality='atac', p_value=0.05)
>>> assert len(organs_with_gene) > 0

>>> organs_with_gene.get_list(values_included=['CASTOR2'])[0]['values'].keys()
dict_keys(['CASTOR2'])

```

`client.select_organs(where='cell', ...)`:
```python
>>> from hubmap_cell_id_gen_py import get_sequencing_cell_id
>>> sequencing_cell_id = get_sequencing_cell_id('210d118a14c8624b6bb9610a9062656e','AAACAACGAAACGTGG')
>>> organs_with_cell = client.select_organs(where='cell', has=[sequencing_cell_id])
>>> assert len(organs_with_cell) > 0

```