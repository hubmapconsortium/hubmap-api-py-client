```python
>>> from hubmap_api_py_client import Client, test_url
>>> client = Client(test_url)

>>> kidney_genes = client.select_genes(where='organ', has=['Kidney'], genomic_modality='rna', p_value=0.05)
>>> kidney_cells = client.select_cells(where='organ', has=['Kidney'])
>>> kidney_genes & kidney_cells
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: Cannot combine queries on two different base models.

>>> client.select_cells(where='fake', has=['VIM>1'], genomic_modality='rna')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['organ', 'gene', 'dataset', 'cluster', 'protein']

>>> client.select_cells(where='gene', has=['VIM>1'], genomic_modality='fake')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['rna', 'atac']

```

