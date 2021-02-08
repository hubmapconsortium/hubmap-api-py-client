`client.select_cells()`:
```python
>>> from hubmap_api_py_client import Client, test_url
>>> client = Client(test_url)

>>> all_cells = client.select_cells()
>>> assert len(all_cells) > 0

```


`client.select_cells(where='gene', ...)`:
```python
>>> cells_with_gene = client.select_cells(where='gene', has=['CASTOR2 > 1'], genomic_modality='rna')
>>> assert len(cells_with_gene) > 0

>>> cells_with_gene_details = cells_with_gene.get_details(10)
>>> cells_with_gene_details[0]['values'].keys()
dict_keys([])

>>> cells_with_gene_details_with_values = cells_with_gene.get_details(10, values_included=['CASTOR2'])
>>> cells_with_gene_details_with_values[0]['values'].keys()
dict_keys(['CASTOR2'])

>>> cells_with_gene_atac = client.select_cells(where='gene', has=['CHN2'], genomic_modality='atac')
>>> assert len(cells_with_gene_atac) > 0

```

`client.select_cells(where='organ', ...)`:
```python
>>> cells_in_kidney = client.select_cells(where='organ', has=['Kidney'])
>>> assert len(cells_in_kidney) > 0

```

`client.select_cells(where='protein', ...)`:
```python
>>> ki67_cells = client.select_cells(where='protein', has=['Ki67>5000'])
>>> assert len(ki67_cells) > 0

>>> ki67_cells_details = ki67_cells.get_details(10)
>>> ki67_cells_details[0]['values'].keys()
dict_keys([])

>>> ki67_cells_details_with_values = ki67_cells.get_details(10, values_included=['Ki67', 'CD20'])
>>> ki67_cells_details_with_values[0]['values'].keys()
dict_keys(['CD20', 'Ki67'])

```

`client.select_cells(where='dataset', ...)`:
```python
>>> cells_in_dataset = client.select_cells(where='dataset', has=['68159e4bd6a2cea1cd66e8f3050cfcb7'])
>>> assert len(cells_in_dataset) > 0

```
