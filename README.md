<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/doublecloud
[pypi-url]: https://pypi.org/project/doublecloud/
[license-image]: https://img.shields.io/github/license/doublecloud/python-sdk.svg
[license-url]: https://github.com/doublecloud/python-sdk/blob/main/LICENSE

# DoubleCloud SDK for Python

Wanna automate your DoubleCloud infrastructure with Python?
Let's start.

## Installation

Run the following in your terminal:

```sh
pip install doublecloud
```

## Getting started

There are a couple of options for authorizing your requests:

* Service Account Keys
* Externally created IAM tokens.

### Service Account Keys

```python
# you can store and read it from a JSON file 
sa_key = {
    "id": "...",
    "service_account_id": "...",
    "private_key": "..."
}

sdk = doublecloud.SDK(service_account_key=sa_key)
```

For more information on how to create a **service account** and **authorized keys**, see the [DoubleCloud documentation](https://double.cloud/docs/en/administration/step-by-step/create-service-account).

### IAM tokens

```python
sdk = doublecloud.SDK(iam_token="t1.9eu...")
```

Check the `examples` directory for more examples.

For step-by-step instructions and examples of how to get an **IAM token** for your service account, see the [DoubleCloud documentation](https://double.cloud/docs/en/public-api/get-iam-token).

## How to contribute

### Dependencies

* Use `make venv` command to install the library, its production and development dependencies.
* Use `make submodule` to fetch proto specifications.
* Use `make generate` to generate wrappers for gRPC services.

### Formatting

Use `make format` to autoformat code with various set of tools.

### Tests

* `make test` to run tests for current python version
* `make lint` to run only linters for current python version
* `make tox-current` to run all checks (tests + code style checks + linters + format check) for current python version
* `make tox` to run all checks for all supported (installed in your system) python versions

### Maintaining

If a pull request consists of several meaningful commits that should be preserved, use the **Rebase and merge** option. Otherwise, use **Squash and merge**.

New release (changelog, tag and pypi upload) will be automatically created on each push to main via **Github Actions** workflow.
