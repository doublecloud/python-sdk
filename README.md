<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/doublecloud
[pypi-url]: https://pypi.org/project/doublecloud/
[build-image]: https://github.com/doublecloud/python-sdk/actions/workflows/run-tests.yml/badge.svg
[build-url]: https://github.com/doublecloud/python-sdk/actions/workflows/run-tests.yml
[license-image]: https://img.shields.io/github/license/doublecloud/python-sdk.svg
[license-url]: https://github.com/doublecloud/python-sdk/blob/main/LICENSE

# DoubleCloud SDK for Python

Wanna automate your doublecloud infrastructure with python?
Let's start.

Installation:

    pip install doublecloud

## Getting started

There are a couple of options for authorization your requests - Service Account Keys and externally created IAM tokens.

### Service Account Keys

```python
# you can store and read it from JSON file 
sa_key = {
    "id": "...",
    "service_account_id": "...",
    "private_key": "..."
}

sdk = doublecloud.SDK(service_account_key=sa_key)
```

### IAM tokens

```python
sdk = doublecloud.SDK(iam_token="t1.9eu...")
```

Check `examples` directory for more examples.


## Contributing
### Dependencies
Use `make venv` command to install library, its production and development dependencies.

### Formatting
Use `make format` to autoformat code with black tool. 

### Tests
- `make test` to run tests for current python version
- `make lint` to run only linters for current python version
- `make tox-current` to run all checks (tests + code style checks + linters + format check) for current python version
- `make tox` to run all checks for all supported (installed in your system) python versions
- `make test-all-versions` to run all checks for all supported python versions in docker container


### Maintaining
If pull request consists of several meaningful commits, that should be preserved, 
then use "Rebase and merge" option. Otherwise use "Squash and merge". 

New release (changelog, tag and pypi upload) will be automatically created 
on each push to main via Github Actions workflow.
