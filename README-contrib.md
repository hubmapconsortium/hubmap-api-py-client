## Development

From a checkout of the repo, install and run tests::
```sh
pip install -r requirements.txt
pip install -r requirements-dev.txt
./test.sh
```

To build and publish, make sure you have a `.pypirc` with a token,
and then run `./publish.sh`.
