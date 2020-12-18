# cells-api-py-client
Python client for the [HuBMAP Cells API](https://github.com/hubmapconsortium/cross_modality_query);
See also: [`cells-api-js-client`](https://github.com/hubmapconsortium/cells-api-js-client#readme).

Contributors start [here](https://github.com/hubmapconsortium/cells-api-py-client/blob/main/README-contrib.md#readme).

## Usage

Install from pypi:
```
pip install cells-api-py-client
```

Find cells with different criteria, and intersect resulting sets:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> cells_with_vim = client.query_genes('cell', ['VIM > 0.5'], genomic_modality='rna')
>>> assert len(cells_with_vim) > 0

# Select cells from the datasets with the following UUIDs:
>>> dataset_a = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> dataset_b = 'e8d642084fc5ec8b5d348ebab96a4b22'
>>> cells_in_datasets = \
...     client.query_datasets('cell', [dataset_a]) \
...     | client.query_datasets('cell', [dataset_b])
>>> assert len(cells_in_datasets) > 0

# Combine criteria with intersection:
>>> cells_with_vim_in_datasets = cells_with_vim & cells_in_datasets

# Get a list; should run quickly:
>>> cell_list = cells_with_vim_in_datasets.get_list(10)
>>> assert len(cell_list) == 10
>>> assert cell_list[0].keys() == {'cell_id', 'modality', 'dataset', 'clusters', 'protein_mean', 'protein_total', 'protein_covar'}

```

Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> kidney_genes = client.query_organs('gene', ['Kidney'], genomic_modality='rna', p_value=0.05)
>>> kidney_genes_details = kidney_genes.get_details(10)
>>> assert kidney_genes_details[0].keys() == {'gene_symbol', 'go_terms', 'values'}

```

Find organs that differentially express the gene VIM at the 0.01 significance level
```python
>>> from cells_api_py_client import Client
>>> client = Client('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_vim = client.query_genes('organ', ['VIM'], genomic_modality='rna', p_value=0.01)
>>> organs_with_vim_details = organs_with_vim.get_details(10)
>>> assert organs_with_vim_details[0].keys() == {'grouping_name', 'values'}

```
