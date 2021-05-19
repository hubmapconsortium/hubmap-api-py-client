`client.select_cells()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_cells = client.select_cells()
>>> assert len(all_cells) > 0

```


`client.select_cells(where='gene', ...)`:
```python
>>> gene_symbol = client.select_genes().get_list()[0]['gene_symbol']
>>> cells_with_gene = client.select_cells(where='gene', has=[f'{gene_symbol} > 1'], genomic_modality='rna')
>>> assert len(cells_with_gene) > 0

>>> cells_with_gene_details_with_values = cells_with_gene.get_list(values_included=[gene_symbol])
>>> cells_keys = cells_with_gene_details_with_values[0]['values'].keys()
>>> assert list(cells_keys) == [gene_symbol]

>>> gene_symbol = client.select_genes().get_list()[10]['gene_symbol']
>>> cells_with_gene_atac = client.select_cells(where='gene', has=[gene_symbol], genomic_modality='atac')
>>> assert len(cells_with_gene_atac) > 0

```

`client.select_cells(where='organ', ...)`:
```python
>>> organ_name = client.select_organs().get_list()[0]['grouping_name']
>>> cells_in_organ = client.select_cells(where='organ', has=[organ_name])
>>> assert len(cells_in_organ) > 0

```

`client.select_cells(where='protein', ...)`:
```python
>>> protein_name = client.select_proteins().get_list()[0]['protein_id']
>>> protein_cells = client.select_cells(where='protein', has=[f'{protein_name}>5000'])
>>> assert len(protein_cells) > 0

>>> protein_cells_details_with_values = protein_cells.get_list(values_included=[protein_name])[0:10]
>>> protein_keys = protein_cells_details_with_values[0]['values'].keys()
>>> assert list(protein_keys) == [protein_name]

```

`client.select_cells(where='dataset', ...)`:
```python
>>> dataset_uuid = client.select_datasets().get_list()[0]['uuid']
>>> cells_in_dataset = client.select_cells(where='dataset', has=[dataset_uuid])
>>> assert len(cells_in_dataset) > 0

```
