0.0.5
- Support queries for and by dataset
- Support queries for all entities by identifier
- Examples of query by cluster
- Example of query for cell by protein
- Reworking client-side parameter validation

0.0.4 - in progress
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
