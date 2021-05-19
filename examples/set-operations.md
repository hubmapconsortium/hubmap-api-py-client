Providing a list to `has` is the same as using `|` for the union:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> datasets = client.select_datasets().get_list()
>>> a_uuid = datasets[0]['uuid']
>>> b_uuid = datasets[1]['uuid']

>>> a_cells = client.select_cells(where='dataset', has=[a_uuid])
>>> b_cells = client.select_cells(where='dataset', has=[b_uuid])

>>> len_a_cells = len(a_cells)
>>> len_b_cells = len(b_cells)

>>> assert len_a_cells > 0
>>> assert len_b_cells > 0

>>> a_b_union_cells = \
...     client.select_cells(where='dataset', has=[a_uuid]) \
...     | client.select_cells(where='dataset', has=[b_uuid])
>>> a_b_cells = \
...     client.select_cells(where='dataset', has=[a_uuid, b_uuid])

>>> len_a_b_cells = len(a_b_cells)
>>> assert len_a_b_cells == len(a_b_union_cells)
>>> assert len_a_b_cells == len_a_cells + len_b_cells

```

Intersection and difference are also available:
```python
>>> gene_symbol = client.select_genes().get_list()[10]['gene_symbol']
>>> gene_cells = client.select_cells(where='gene', has=[f'{gene_symbol} > 0.5'], genomic_modality='rna')
>>> a_b_gene_cells = a_b_cells & gene_cells
>>> a_b_no_gene_cells = a_b_cells - gene_cells
>>> assert len(a_b_gene_cells) + len(a_b_no_gene_cells) == len_a_b_cells

```
