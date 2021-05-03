Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> li_genes = client.select_genes(where='organ', has=['Large Intestine'], genomic_modality='rna', p_value=0.05)
>>> li_genes_details = li_genes.get_list()[0:10]
>>> li_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms'])

```

Find organs that differentially express the gene VIM at the 0.01 significance level
```python
>>> organs_with_vim = client.select_organs(where='gene', has=['VIM'], genomic_modality='rna', p_value=0.01)
>>> organs_with_vim_details = organs_with_vim.get_list()[0:10]
>>> organs_with_vim_details[0].keys()
dict_keys(['grouping_name'])

```