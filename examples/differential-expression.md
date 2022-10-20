Find genes differentially expressed by the kidney at significance level 0.05:

```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> modality = 'atac'
>>> gene_symbol = client.select_genes(where='modality', has=[modality]).get_list()[0]['gene_symbol']
>>> organs_with_gene = client.select_organs(where='gene', has=[gene_symbol], genomic_modality=modality, p_value=1.0)
>>> organs_with_gene_details = organs_with_gene.get_list()[0:10]
>>> organs_with_gene_details[0].keys()
dict_keys(['grouping_name'])

```

Note: 'grouping_name' is used to refer to identifiers for different groupings of cells including organs and clusters


Find genes differentially expressed by the organ at significance level 1.0:

```python
>>> organ_name = organs_with_gene_details[0]['grouping_name']
>>> organ_genes = client.select_genes(where='organ', has=[organ_name], genomic_modality='atac', p_value=1.0)
>>> organ_genes_details = organ_genes.get_list()[0:10]
>>> organ_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'summary'])

```