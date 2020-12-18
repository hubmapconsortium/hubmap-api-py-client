# cells-api-py-client
Python client for the [HuBMAP Cells API](https://github.com/hubmapconsortium/cross_modality_query);
See also: [`cells-api-js-client`](https://github.com/hubmapconsortium/cells-api-js-client#readme).

Contributors start [here](https://github.com/hubmapconsortium/cells-api-py-client/blob/main/README-contrib.md#readme).

## Usage

Install from pypi:
```
pip install cells-api-py-client
```
and then:

```python
>>> from cells_api_py_client.external import ExternalClient
>>> from cells_api_py_client.internal import InternalClient

>>> ex_client = ExternalClient('https://cells.dev.hubmapconsortium.org/api/')
>>> in_client = InternalClient('https://cells.dev.hubmapconsortium.org/api/')

>>> cells_with_vim = ex_client.query('gene', 'cell', ['VIM > 0.5'], genomic_modality='rna')
>>> assert len(cells_with_vim) > 0

# Show me cells from the datasets with the following UUIDs:

>>> dataset_a = '68159e4bd6a2cea1cd66e8f3050cfcb7'
>>> dataset_b = 'e8d642084fc5ec8b5d348ebab96a4b22'
>>> cells_in_datasets_union = (
...     ex_client.query('dataset', 'cell', [dataset_a])
...     | ex_client.query('dataset', 'cell', [dataset_b])
... )

# TODO: Not working: magic method result is empty:

>>> len(cells_in_datasets_union)
0

# Alternatively, unions can be created by supplying a list, but results are the same:
>>> cells_in_datasets = ex_client.query('dataset', 'cell', [dataset_a, dataset_b])

# TODO: >>> assert len(cells_in_datasets) == len(cells_in_datasets_union)

# Combine criteria with intersection:
>>> cells_with_vim_in_datasets = cells_with_vim & cells_in_datasets
>>> cell_details = cells_with_vim_in_datasets.get_list(10)
>>> assert len(cell_details) == 10
>>> assert cell_details[0].keys() == {'cell_id', 'modality', 'dataset', 'clusters', 'protein_mean', 'protein_total', 'protein_covar'}

# Show me genes differentially expressed by the kidney at significance level 0.05

>>> output_type = 'gene'
>>> input_type = 'organ'
>>> input_set = ['Kidney']
>>> p_value = 0.05
>>> genomic_modality = 'rna'

>>> gene_set = in_client.hubmap_query(input_type, output_type, input_set, genomic_modality, p_value=p_value)
>>> gene_set_details = in_client.set_detail_evaluation(gene_set, "gene", 10, values_included=['Kidney'], values_type='organ')
>>> assert gene_set_details[0].keys() == {'gene_symbol', 'go_terms', 'values'}

# Show me organs that differentially express the gene VIM at the 0.01 significance level

>>> output_type = 'organ'
>>> input_type = 'gene'
>>> input_set = ['VIM']
>>> p_value = 0.01
>>> genomic_modality = 'rna'

>>> organ_set = in_client.hubmap_query(input_type, output_type, input_set, genomic_modality, p_value=p_value)
>>> organ_set_details = in_client.set_detail_evaluation(organ_set, "organ", 10, values_included=['VIM'], values_type='gene')
>>> assert organ_set_details[0].keys() == {'grouping_name', 'values'}

```
