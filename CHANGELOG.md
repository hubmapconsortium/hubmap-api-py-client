0.0.7 - in progress
- Support iteration over result sets.
- Add python environments to gitignore.

0.0.6 - 2021-03-24
- Parameterize api endpoint doctests.
- Only use POST, for simplicity.
- Use values_included appropriately.
- Values in error are sorted.
- Run tests in parallel.
- Remove `get_list` from external interface.
- Distinguish `ResultsSet` from `ResultsList`.
- Remove `values_type` parameter
- `ResultsList` supports `[]`
- Generate pydocs, with accurate kwarg lists..
- Updating doc tests, adding new query type
- Add new parameter to enable gene->dataset and protein->dataset queries

0.0.5 - 2021-02-06
- Support queries for and by dataset
- Support queries for all entities by identifier
- Examples of query by cluster
- Example of query for cell by protein
- Reworking client-side parameter validation
- Integrating hubmap_cell_id_gen_py into examples
- Supporting queries for all entities of a particular type, including proteins
- Expanding table in readme
- Fewer preflight checks on requests: These are a maintenance burden.

0.0.4 - 2021-01-11
- Remove complement magic method, and add difference.
- Require "has" param to be list, and update examples.
- Add subtypes of ResultsSet, and check that operands on set operations match.
- Issue templates
- Rename repo and package.
- Move to github CI
- Add ASCT-B to matrix in README
- Improve input validation logic
- Use slice syntax to get list

0.0.3
- Change to more fluent SDK: `select_TARGET(where='SOURCE', has='CRITERIA', ...)`

0.0.2
- OO interface: Fewer details need to be repeated across methods, because they are kept in the object.

0.0.1
- Basic python interface: methods mirror API hits.
