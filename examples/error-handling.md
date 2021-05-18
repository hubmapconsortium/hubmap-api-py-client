```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> organ_name = client.select_organs().get_list()[0]['grouping_name']
>>> organ_genes = client.select_genes(where='organ', has=[organ_name], genomic_modality='rna', p_value=0.05)
>>> organ_cells = client.select_cells(where='organ', has=[organ_name])
>>> organ_genes & organ_cells
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: Cannot combine queries on two different base models.

>>> gene_symbol = client.select_genes().get_list()[0]['gene_symbol']
>>> client.select_cells(where='fake', has=[f"{gene_symbol}>1"], genomic_modality='rna')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['cell', 'cluster', 'dataset', 'gene', 'organ', 'protein']

>>> client.select_cells(where='gene', has=[f"{gene_symbol}>1"], genomic_modality='fake')
Traceback (most recent call last):
...
hubmap_api_py_client.errors.ClientError: fake not in ['atac', 'rna']

```

