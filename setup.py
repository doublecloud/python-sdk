from setuptools import find_packages, setup

packages = find_packages(".", include=["doublecloud*"])

__version__ = "0.8.0"

setup(
    name="doublecloud",
    version=__version__,
    description="The Double.Cloud official SDK",
    url="https://github.com/doublecloud/python-sdk",
    author="DoubleCloud GmbH",
    author_email="support@double.cloud",
    license="Apache License 2.0",
    install_requires=[
        "cryptography>=39.0.2",
        "grpcio>=1.51.3",
        "protobuf>=4.22.1",
        "grpcio-tools>=1.51.3",
        "googleapis-common-protos>=1.58.0",
        "pyjwt>=2.6.0",
        "requests>=2.28.2",
        "six>=1.16.0",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    tests_require=["pytest"],
    setup_requires=["wheel"],
    packages=packages,
    package_data={"doublecloud": ["*.pyi", "**/*.pyi"]},
    zip_safe=False,
)
