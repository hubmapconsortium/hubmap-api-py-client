```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> li_genes = client.select_genes(where='organ', has=['Large Intestine'], genomic_modality='rna', p_value=0.05)
>>> li_cells = client.select_cells(where='organ', has=['Large Intestine'])
>>> li_genes & li_cells
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: Cannot combine queries on two different base models.

>>> client.select_cells(where='fake', has=['VIM>1'], genomic_modality='rna')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['cell', 'cluster', 'dataset', 'gene', 'organ', 'protein']

>>> client.select_cells(where='gene', has=['VIM>1'], genomic_modality='fake')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['atac', 'rna']

```

