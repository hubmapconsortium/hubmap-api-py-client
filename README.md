# cells-api-py-client
Python client for the [Cells API](https://github.com/hubmapconsortium/cross_modality_query);
See also: [`cells-api-js-client`](https://github.com/hubmapconsortium/cells-api-js-client#readme).

Contributors start [here](https://github.com/hubmapconsortium/cells-api-py-client/blob/main/README-contrib.md#readme).

```python
>>> from cells_api_py_client.internal import *
>>> output_type = 'cell'
>>> input_type = 'gene'
>>> input_set = ['VIM > 0.5']
>>> logical_operator = "and"
>>> genomic_modality = 'rna'

>>> gene_cells = hubmap_query(input_type, output_type, input_set, genomic_modality)
>>> assert set_count(gene_cells, "cell") > 0

# Show me cells from the datasets with the following UUIDs

>>> output_type = 'cell'
>>> input_type = 'dataset'
>>> input_set = ['68159e4bd6a2cea1cd66e8f3050cfcb7', 'e8d642084fc5ec8b5d348ebab96a4b22']

>>> dataset_cells = hubmap_query(input_type, output_type, input_set)
>>> assert set_count(dataset_cells, "cell") > 0

>>> key_one = dataset_cells
>>> key_two = gene_cells
>>> set_type = "cell"

>>> intersection_cells = set_intersection(key_one, key_two, set_type)

>>> cell_details = set_list_evaluation(intersection_cells, "cell", 10)
>>> assert len(cell_details) == 10
>>> assert cell_details[0].keys() == {'cell_id', 'modality', 'dataset', 'clusters', 'protein_mean', 'protein_total', 'protein_covar'}

# Show me genes differentially expressed by the kidney at significance level 0.05

>>> output_type = 'gene'
>>> input_type = 'organ'
>>> input_set = ['Kidney']
>>> p_value = 0.05
>>> genomic_modality = 'rna'

>>> gene_set = hubmap_query(input_type, output_type, input_set, genomic_modality, p_value=p_value)
>>> gene_set_details = set_detail_evaluation(gene_set, "gene", 10, values_included=['Kidney'], values_type='organ')
>>> assert gene_set_details[0].keys() == {'gene_symbol', 'go_terms', 'values'}

# Show me organs that differentially express the gene VIM at the 0.01 significance level

>>> output_type = 'organ'
>>> input_type = 'gene'
>>> input_set = ['VIM']
>>> p_value = 0.01
>>> genomic_modality = 'rna'

>>> organ_set = hubmap_query(input_type, output_type, input_set, genomic_modality, p_value=p_value)
>>> organ_set_details = set_detail_evaluation(organ_set, "organ", 10, values_included=['VIM'], values_type='gene')
>>> assert organ_set_details[0].keys() == {'grouping_name', 'values'}

```
