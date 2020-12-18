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

>>> cells_with_vim = client.query_genes(output='cell', q='VIM > 0.5', genomic_modality='rna')
>>> assert len(cells_with_vim) > 0

# Select cells from the datasets with the following UUIDs:
>>> dataset_a_uuid = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> dataset_b_uuid = 'e8d642084fc5ec8b5d348ebab96a4b22'
>>> cells_in_datasets = \
...     client.query_datasets(output='cell', q=dataset_a_uuid) \
...     | client.query_datasets(output='cell', q=dataset_b_uuid)
>>> assert len(cells_in_datasets) > 0

# Combine criteria with intersection:
>>> cells_with_vim_in_datasets = cells_with_vim & cells_in_datasets

# Get a list; should run quickly:
>>> cell_list = cells_with_vim_in_datasets.get_list(10)
>>> assert len(cell_list) == 10
>>> assert cell_list[0].keys() == {'cell_id', 'modality', 'dataset', 'clusters', 'protein_mean', 'protein_total', 'protein_covar'}

```

[More examples](https://github.com/hubmapconsortium/cells-api-py-client/blob/main/examples/)