from hubmap_api_py_client.internal import InternalClient

_default_limit = 1000


class ExternalClient():
    '''
    The Client provides methods for querying different entity types.
    The methods return ResultSets which can be combined with set operators,
    and then finally evaluated to get the actual data.
    '''

    def __init__(self, base_url):
        self.client = InternalClient(base_url)

    def __repr__(self):
        return f'<Client base_url={self.client.base_url}>'

    def _query(
            self,
            input_type=None, output_type=None, has=None,
            genomic_modality=None, p_value=None, logical_operator=None,
            ResultsSetSubclass=None):
        if not isinstance(has, list) and input_type is not None:
            raise TypeError(f'"has" parameter must be a list, not {has}')
        handle = self.client.hubmap_query(input_type, output_type, has, genomic_modality,
                                          p_value, logical_operator)
        return ResultsSetSubclass(
            self.client, handle,
            input_type=input_type, output_type=output_type,
            query=has
        )


class ResultsSet():
    '''
    Instances of ResultsSet subclasses can be combined with set operators,
    and then prepared for evaluation by calling get_list(),
    which returns a ResultsList.
    '''
    def __init__(
            self, client, handle,
            input_type=None, output_type=None,
            query=None):
        '''
        Do not call the constructor directly:
        Instead, use the select_* methods on Client.
        '''
        self.client = client
        self.handle = handle
        self.input_type = input_type
        self.output_type = output_type
        self.query = query

    def __repr__(self):
        return (
            f'<{_class_name(self.output_type)} '
            f'base_url={self.client.base_url} handle={self.handle}>')

    def __len__(self):
        return self.client.set_count(self.handle, self.output_type)

    def __or__(self, other_set):
        return self._operation(other_set, self.client.set_union)

    def __and__(self, other_set):
        return self._operation(other_set, self.client.set_intersection)

    def __sub__(self, other_set):
        return self._operation(other_set, self.client.set_difference)

    def _operation(self, other_set, method):
        new_handle = method(self.handle, other_set.handle, self.output_type)
        return ResultsSet(
            self.client, new_handle,
            input_type=self.input_type, output_type=self.output_type,
            query=self.query)

    def get_list(self, values_included=[], sort_by=None):
        return ResultsList(
            results_set=self,
            values_included=values_included,
            sort_by=sort_by)


class ResultsList():
    '''
    Use subscript syntax, ie [start, end], to get data
    from a ResultsList.
    '''
    def __init__(
            self, results_set,
            values_included=[], sort_by=None):
        '''
        Do not call the constructor directly:
        Instead use the get_list method of ResultsSet.
        '''
        self.results_set = results_set
        self.values_included = values_included
        self.sort_by = sort_by

    def __repr__(self):
        return (
            f'<ResultsList results_set={self.results_set} '
            f'values_included={self.values_included} sort_by={self.sort_by}>')

    def __len__(self):
        return len(self.results_set)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                raise NotImplementedError('Negative indexes not implemented')
            limit = 1
            offset = key
            return self._get(limit, offset)[0]
        if isinstance(key, slice):
            if key.step:
                raise NotImplementedError('step not implemented')
            if key.start < 0:
                raise NotImplementedError('Negative indexes not implemented')
            limit = key.stop - key.start
            offset = key.start
            return self._get(limit, offset)
        raise TypeError()

    def _get(self, limit, offset):
        if not self.values_included and not self.sort_by:
            return self.results_set.client.set_list_evaluation(
                self.results_set.handle,
                self.results_set.output_type,
                limit=limit, offset=offset)
        return self.results_set.client.set_detail_evaluation(
            self.results_set.handle,
            self.results_set.output_type,
            limit=limit, offset=offset,
            sort_by=self.sort_by,
            values_included=self.values_included)


def _class_name(output_type):
    return f'{output_type.capitalize()}ResultsSet'


def _create_subclass(output_type):
    return type(_class_name(output_type), (ResultsSet,), {})


def _add_method(output_type, ResultsSetSubclass, doc):
    method_name = f'select_{output_type}s'
    method = (
        lambda self, where=None, has=None,
        genomic_modality=None, p_value=None,
        logical_operator=None:
        self._query(
            input_type=where, output_type=output_type, has=has,
            genomic_modality=genomic_modality, p_value=p_value,
            logical_operator=logical_operator,
            ResultsSetSubclass=ResultsSetSubclass)
    )
    method.__doc__ = doc
    setattr(ExternalClient, method_name, method)


for output_type, doc in {
    'cell':
    '''
    Select a set of cells. If no params are provided, selects the set of all cells.
    Otherwise, selects a set of cells filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query, must be one of
            ["cell", "gene", "protein", "organ", "dataset"]
        has->List[str] A list of entities or expressions supplied as input to the query
        genomic_modality->str Modality to consider in quantitative queries.
            Required for queries in which "where" is "gene". Must be one of ["rna", "atac"].
        logical_operator->str The logical operator applied to filters generated by elements of has.
            Required for queries in which "where" is "gene" or "protein" and
            "has" contains more than one element. Must be one of ["and", "or"].
    ''',
    'organ':
    '''
    Select a set of organs. If no params are provided, selects the set of all organs.
    Otherwise, selects a set of organs filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query. Must be one of
            ["gene", "organ"].
        has->List[str] A list of entities supplied as input to the query
        genomic_modality->str Modality to consider for quantitative queries.
            Required for queries in which "where" is "gene". Must be one of ["rna", "atac"].
        p_value->float Threshold of significance applied to gene-organ associations.
            Required for queries in which "where" is "gene." Must be between 0 and 1.
        logical_operator->str The logical operator applied to filters generated by elements of has.
            Required for queries in which "where" is "gene" and "has"
            contains more than one element. Must be one of ["and", "or"].
    ''',
    'gene':
    '''
    Select a set of genes. If no params are provided, selects the set of all genes.
    Otherwise, selects a set of genes filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query, must be one of
            ["gene", "organ", "cluster"].
        has->List[str] A list of entities or supplied as input to the query
        genomic_modality->str Modality to consider for quantitative queries.
            Required for queries in which "where" is "organ" or "cluster".
            Must be one of ["rna", "atac"].
        p_value->float Threshold of significance applied to gene-organ and gene-cluster
            associations. Required for queries in which "where" is "organ" or "cluster."
            Must be between 0 and 1.
        logical_operator->str The logical operator applied to filters generated by elements of has.
            Required for queries in which "where" is "organ" or "cluster" and
            "has" contains more than one element. Must be one of ["and", "or"].
    ''',
    'cluster':
    '''
    Select a set of clusters. If no params are provided, selects the set of all clusters.
    Otherwise, selects a set of clusters filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query.
            Must be one of ["gene", "cluster", "dataset"].
        has->List[str] A list of entities supplied as input to the query
        genomic_modality->str Modality to consider for quantitative queries.
            Required for queries in which "where" is "gene". Must be one of ["rna", "atac"].
        p_value->float Threshold of significance applied to gene-cluster associations.
            Required for queries in which "where" is "gene." Must be between 0 and 1.
        logical_operator->str The logical operator applied to filters generated by elements of has.
            Required for queries in which "where" is "gene" and "has" contains
            more than one element. Must be one of ["and", "or"].
    ''',
    'dataset':
    '''
    Select a set of datasets. If no params are provided, selects the set of all datasets.
    Otherwise, selects a set of datasets filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query.
            Must be one of ["dataset", "cell", "cluster"].
        has->List[str] A list of entities supplied as input to the query.
    ''',
    'protein':
    '''
    Select a set of proteins. If no params are provided, selects the set of all proteins.
    Otherwise, selects a set of proteins filtered based on parameters supplied.
        where->str The type of entity being supplied as input to query.
            Must be one of ["protein"].
        has->List[str] A list of entities supplied as input to the query.
    '''

}.items():
    ResultsSetSubclass = _create_subclass(output_type)
    _add_method(output_type, ResultsSetSubclass, doc)
