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
if ( python --version 2>&1 | grep '3.6' ); then
  echo 'pydoc on 3.6 has a different output format; skipping...'
else
  for CLASS in Client external.ResultsSet external.ResultsList; do
    echo "Docs up-to-date for $CLASS?"
    CMD="python -m pydoc hubmap_api_py_client.$CLASS"
    echo "Running: $CMD"
    TARGET="README-$CLASS.txt"
    diff $TARGET <($CMD) || die "To update: $CMD > $TARGET"
  done
fi
end pydoc

start pytest
CMD='API_ENDPOINT="https://cells.api.hubmapconsortium.org/api/" PYTHONPATH="${PYTHONPATH}:hubmap_api_py_client" pytest --numprocesses auto -vv --doctest-glob="*.md"'
echo $CMD
eval $CMD
end pytest

start changelog
if [ "$TRAVIS_BRANCH" != 'main' ]; then
  diff CHANGELOG.md <(curl -s https://raw.githubusercontent.com/hubmapconsortium/hubmap-api-py-client/main/CHANGELOG.md) \
    && die 'Update CHANGELOG.md'
fi
end changelog
