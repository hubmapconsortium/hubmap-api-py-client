`client.select_genes()`:
```python
>>> from os import environ
>>> from hubmap_api_py_client import Client
>>> client = Client(environ['API_ENDPOINT'])

>>> all_genes = client.select_genes()
>>> assert len(all_genes) > 0

```

`client.select_genes(where='organ', ...)`:
```python
>>> gene_symbol = client.select_genes(where="modality", has=["rna"]).get_list()[0]['gene_symbol']
>>> organs_with_gene = client.select_organs(where='gene', has=[gene_symbol], genomic_modality='rna', p_value=1.0)
>>> organs_with_gene_details = organs_with_gene.get_list()[0:10]
>>> organ_name = organs_with_gene_details[0]['grouping_name']
>>> organ_genes = client.select_genes(where='organ', has=[organ_name], genomic_modality='rna', p_value=1.0)

>>> organ_genes_details = organ_genes.get_list()
>>> organ_genes_details[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'summary'])

>>> organ_genes_details_with_values = organ_genes.get_list(values_included=[organ_name])
>>> organ_genes_details_with_values[0].keys()
dict_keys(['gene_symbol', 'go_terms', 'summary', 'values'])

>>> organ_keys = organ_genes_details_with_values[0]['values'].keys()
>>> assert list(organ_keys) == [organ_name]

```

`client.select_genes(where='cluster', ...)`:
```python
>>> modality = "rna"
>>> rna_dataset = client.select_datasets(where="modality", has=[modality]).get_list()[0]["uuid"]
>>> rna_cluster = client.select_clusters(where="dataset", has=[rna_dataset]).get_list()[0]["grouping_name"]
>>> rna_cluster_genes = client.select_genes(where="cluster",has=[rna_cluster], genomic_modality=modality, p_value=1.0)
>>> assert len(rna_cluster_genes) > 0

```
