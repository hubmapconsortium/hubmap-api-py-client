# hubmap-api-py-client
[![PyPI version](https://badge.fury.io/py/hubmap-api-py-client.svg)](https://pypi.org/project/hubmap-api-py-client/)

Python client for the [HuBMAP Cells API](https://github.com/hubmapconsortium/cross_modality_query);
See also: [`hubmap-api-js-client`](https://github.com/hubmapconsortium/hubmap-api-js-client#readme).

Contributors start [here](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/README-contrib.md#readme).

## Usage

Install from pypi:
```
pip install hubmap-api-py-client
```

Find cells with different criteria, and intersect resulting sets:
```shell
$ export API_ENDPOINT='https://cells.dev.hubmapconsortium.org/api/'
```
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> [m for m in dir(client) if m.startswith('select_')]
['select_cells', 'select_clusters', 'select_datasets', 'select_genes', 'select_organs', 'select_proteins']

>>> cells_with_vim = client.select_cells(where='gene', has=['VIM > 0.5'], genomic_modality='rna')
>>> assert len(cells_with_vim) > 0

# Select cells from the datasets with the following UUIDs:
>>> dataset_a_uuid = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> dataset_b_uuid = 'e8d642084fc5ec8b5d348ebab96a4b22'
>>> cells_in_a_len = len(client.select_cells(where='dataset', has=[dataset_a_uuid]))
>>> cells_in_b_len = len(client.select_cells(where='dataset', has=[dataset_b_uuid]))
>>> cells_in_datasets = client.select_cells(where='dataset', has=[dataset_a_uuid, dataset_b_uuid])
>>> cells_in_datasets_len = len(cells_in_datasets)
>>> assert cells_in_datasets_len > 0
>>> assert cells_in_datasets_len == cells_in_a_len + cells_in_b_len

# Combine criteria with intersection:
>>> cells_with_vim_in_datasets = cells_with_vim & cells_in_datasets
>>> assert len(cells_with_vim_in_datasets) > 10

# Get a list; should run quickly:
>>> cell_list = cells_with_vim_in_datasets.get_list()

>>> cells = cell_list[0:10]
>>> assert len(cells) == 10
>>> assert cells[0].keys() == {'cell_id', 'modality', 'dataset', 'organ', 'clusters'}

```

More documentation:
- [Examples](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/)
- [`Client` pydoc](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/README-Client.txt)
- [`ResultsSet` pydoc](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/README-external.ResultsSet.txt)
- [`ResultsList` pydoc](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/README-external.ResultsList.txt)


Only some types of objects can be retrieved from other types of objects:

| `where=...`       | None    | `cell`    | `cluster` | `dataset` | `gene`    | `organ`   | `protein` |
| ----------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [`select_cells()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_cells.md)                                                                                                              | ✓         | ✓         |           | ✓         | ✓         | ✓         | ✓         |
| [`select_clusters()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_clusters.md)                                                                                                              | ✓         |           | ✓         | ✓         | ✓ ✩       | ✩         | ✩         |
| [`select_datasets()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_datasets.md)| ✓         | ✓         | ✓         | ✓         |           |✶          |           |
| [`select_genes()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_genes.md)                                                                                                              | ✓         |           | ✓ ✩       |           | ✓         | ✓ ✩       | ✩         |
| [`select_organs()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_organs.md)                                                                                                              | ✓         | ✓         | ✩         | ✶         | ✓ ✩       | ✓         | ✩         |
| [`select_proteins()`](https://github.com/hubmapconsortium/hubmap-api-py-client/blob/main/examples/select_organs.md)                                                                                                          | ✓         |           | ✩         |           | ✩         | ✩         |           |

- "✓" = Supported by Cells API, and this client.
- "✶" = Supported by Entities API; support in this client is [on the roadmap](https://github.com/hubmapconsortium/hubmap-api-py-client/issues/25).
- "✩" = Possible connection to [ASCT-B](https://hubmapconsortium.github.io/ccf-asct-reporter/vis?sheet=all&dataVersion=latest) (Anatomical Structures / Cell Types / Biomarkers)
