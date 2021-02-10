Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from hubmap_api_py_client import Client, test_url
>>> client = Client(test_url)

>>> kidney_genes = client.select_genes(where='organ', has=['Kidney'], genomic_modality='rna', p_value=0.05)
>>> kidney_genes_details = kidney_genes.get_details(10)
>>> kidney_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

```

Find organs that differentially express the gene VIM at the 0.01 significance level
```python
>>> organs_with_vim = client.select_organs(where='gene', has=['VIM'], genomic_modality='rna', p_value=0.01)
>>> organs_with_vim_details = organs_with_vim.get_details(10)
>>> organs_with_vim_details[0].keys()
dict_keys(['grouping_name'])

```