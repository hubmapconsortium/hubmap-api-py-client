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
>>> from cells_api_py_client.external import ExternalClient
>>> ex_client = ExternalClient('https://cells.dev.hubmapconsortium.org/api/')

>>> cells_with_vim = ex_client.query('gene', 'cell', ['VIM > 0.5'], genomic_modality='rna')
>>> assert len(cells_with_vim) > 0

# Select cells from the datasets with the following UUIDs:
>>> dataset_a = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> dataset_b = 'e8d642084fc5ec8b5d348ebab96a4b22'
>>> cells_in_datasets = ex_client.query('dataset', 'cell', [dataset_a, dataset_b])
>>> assert len(cells_in_datasets) > 0

# Alternatively, use an operator to create union:
# TODO: Not working: magic method result is empty!
>>> cells_in_datasets_union = (
...     ex_client.query('dataset', 'cell', [dataset_a])
...     | ex_client.query('dataset', 'cell', [dataset_b])
... )
>>> len(cells_in_datasets_union)
0

# TODO: >>> assert len(cells_in_datasets) == len(cells_in_datasets_union)

# Combine criteria with intersection:
>>> cells_with_vim_in_datasets = cells_with_vim & cells_in_datasets

# Get a list; should run quickly:
>>> cell_list = cells_with_vim_in_datasets.get_list(10)
>>> assert len(cell_list) == 10
>>> assert cell_list[0].keys() == {'cell_id', 'modality', 'dataset', 'clusters', 'protein_mean', 'protein_total', 'protein_covar'}

```

Find genes differentially expressed by the kidney at significance level 0.05:
```python
>>> from cells_api_py_client.external import ExternalClient
>>> ex_client = ExternalClient('https://cells.dev.hubmapconsortium.org/api/')

>>> kidney_genes = ex_client.query('organ', 'gene', ['Kidney'], genomic_modality='rna', p_value=0.05)
>>> kidney_genes_details = kidney_genes.get_details(10, values_included=['Kidney'], values_type='organ')
>>> assert kidney_genes_details[0].keys() == {'gene_symbol', 'go_terms', 'values'}

```

Find organs that differentially express the gene VIM at the 0.01 significance level
```python
>>> from cells_api_py_client.external import ExternalClient
>>> ex_client = ExternalClient('https://cells.dev.hubmapconsortium.org/api/')

>>> organs_with_vim = ex_client.query('gene', 'organ', ['VIM'], genomic_modality='rna', p_value=0.01)
>>> organs_with_vim_details = organs_with_vim.get_details(10, values_included=['VIM'], values_type='gene')
>>> assert organs_with_vim_details[0].keys() == {'grouping_name', 'values'}

```
