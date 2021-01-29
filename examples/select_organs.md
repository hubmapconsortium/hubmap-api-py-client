`client.select_organs()`:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> all_organs = client.select_organs()
>>> assert len(all_organs) > 0

```

`client.select_organs(where='gene', ...)`:
```python
>>> organs_with_gene = client.select_organs(where='gene', has=['CHN2'], genomic_modality='atac', p_value=0.05)
>>> assert len(organs_with_gene) > 0

```

`client.select_organs(where='cell', ...)`:
```python
>>> from hubmap_cell_id_gen_py import get_sequencing_cell_id
>>> sequencing_cell_id = get_sequencing_cell_id('210d118a14c8624b6bb9610a9062656e','AAACAACGAAACGTGG')
>>> organs_with_cell = client.select_organs(where='cell', has=[sequencing_cell_id])
>>> assert len(organs_with_cell) > 0

```