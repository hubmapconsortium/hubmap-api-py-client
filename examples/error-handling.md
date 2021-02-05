```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> kidney_genes = client.select_genes(where='organ', has=['Kidney'], genomic_modality='rna', p_value=0.05)
>>> kidney_cells = client.select_cells(where='organ', has=['Kidney'])
>>> kidney_genes & kidney_cells
Traceback (most recent call last):
...
ValueError: Operand output types do not match: gene != cell

>>> client.select_cells(where='fake', has=['VIM>1'], genomic_modality='rna')
Traceback (most recent call last):
...
ValueError: fake not in ['cell', 'gene', 'organ', 'protein', 'dataset']

>>> client.select_cells(where='gene', has=['VIM>1'], genomic_modality='fake')
Traceback (most recent call last):
...
hubmap_api_py_client.internal.ApiError

```

