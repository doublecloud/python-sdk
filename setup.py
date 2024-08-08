from setuptools import find_packages, setup

packages = find_packages(".", include=["doublecloud*"])

__version__ = "0.12.0"

setup(
    name="doublecloud",
    version=__version__,
    description="The Double.Cloud official SDK",
    url="https://github.com/doublecloud/python-sdk",
    author="DoubleCloud GmbH",
    author_email="support@double.cloud",
    license="Apache License 2.0",
    install_requires=[
        "cryptography==43.0.0",
        "grpcio==1.65.4",
        "protobuf==5.27.3",
        "grpcio-tools==1.65.4",
        "googleapis-common-protos==1.63.2",
        "pyjwt==2.9.0",
        "requests==2.32.3",
        "six==1.16.0",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    tests_require=["pytest"],
    setup_requires=["wheel"],
    packages=packages,
    package_data={"doublecloud": ["*.pyi", "**/*.pyi"]},
    zip_safe=False,
)
