#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1 || true`
reset=`tput sgr0 || true`

start() { echo "::group::$1"; }
end() { echo "::endgroup::"; }
die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

start flake8
flake8 || die "Try: autopep8 --in-place --aggressive -r ."
end flake8

start pydoc
CMD='python -m pydoc hubmap_api_py_client.Client'
TARGET='README-pydoc.txt'
diff <($CMD) $TARGET || die "To update: $CMD > $TARGET"
end pydoc

start pytest
CMD='PYTHONPATH="${PYTHONPATH}:hubmap_api_py_client" pytest --numprocesses auto -vv --doctest-glob="*.md"'
echo $CMD
eval $CMD
end pytest

start changelog
if [ "$TRAVIS_BRANCH" != 'main' ]; then
  diff CHANGELOG.md <(curl -s https://raw.githubusercontent.com/hubmapconsortium/hubmap-api-py-client/main/CHANGELOG.md) \
    && die 'Update CHANGELOG.md'
fi
end changelog
