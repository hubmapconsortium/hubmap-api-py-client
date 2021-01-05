#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

start() { [[ -z $CI ]] || echo travis_fold':'start:$1; echo ${green}$1${reset}; }
end() { [[ -z $CI ]] || echo travis_fold':'end:$1; }
die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

start flake8
flake8 || die "Try: autopep8 --in-place --aggressive -r ."
end flake8

start pytest
CMD='PYTHONPATH="${PYTHONPATH}:cells_api_py_client" pytest -vv --doctest-glob="*.md"'
echo $CMD
eval $CMD
end pytest

# start changelog
# if [ "$TRAVIS_BRANCH" != 'main' ]; then
#   diff CHANGELOG.md <(curl -s https://raw.githubusercontent.com/hubmapconsortium/cells-api-py-client/main/CHANGELOG.md) \
#     && die 'Update CHANGELOG.md'
# fi
# end changelog
