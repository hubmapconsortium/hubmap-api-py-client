Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> kidney_genes = client.select_genes(where='organ', has=['Kidney'], genomic_modality='rna', p_value=0.05, logical_operator='and')
>>> kidney_genes_details = kidney_genes.get_details(10)
>>> assert kidney_genes_details[0].keys() == {'gene_symbol', 'go_terms', 'values'}

```

Find organs that differentially express the gene VIM at the 0.01 significance level
```python
>>> from hubmap_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_vim = client.select_organs(where='gene', has=['VIM'], genomic_modality='rna', p_value=0.01, logical_operator='and')
>>> organs_with_vim_details = organs_with_vim.get_details(10)
>>> assert organs_with_vim_details[0].keys() == {'grouping_name', 'values'}

```