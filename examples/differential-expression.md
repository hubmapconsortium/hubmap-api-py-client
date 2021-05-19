Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> organ_name = client.select_organs().get_list()[1]['grouping_name']
>>> organ_genes = client.select_genes(where='organ', has=[organ_name], genomic_modality='rna', p_value=0.05)
>>> organ_genes_details = organ_genes.get_list()[0:10]
>>> organ_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

```

Find organs that differentially express the a gene at the 0.01 significance level
```python
>>> gene_symbol = client.select_genes().get_list()[10]['gene_symbol']
>>> organs_with_gene = client.select_organs(where='gene', has=[gene_symbol], genomic_modality='atac', p_value=0.05)
>>> organs_with_gene_details = organs_with_gene.get_list()[0:10]
>>> organs_with_gene_details[0].keys()
dict_keys(['grouping_name'])

```