# Changelog

<!--next-version-placeholder-->

## v0.14.0 (2024-09-19)

### Feature

* Revert upgrade for compatibility reasons ([`6f57bd6`](https://github.com/doublecloud/python-sdk/commit/6f57bd6639348c70bce288071e070868c9462de1))

## v0.13.0 (2024-09-19)

### Feature

* Dependobot sec update ([`ecd4af3`](https://github.com/doublecloud/python-sdk/commit/ecd4af3f16b8a151911f97ca0d39f50b96ce7c90))
* Update readme ([`2eb55e2`](https://github.com/doublecloud/python-sdk/commit/2eb55e27826c3b5e63650dc8a692eee16dd8924e))
* Ignore generated code ([`dfbc403`](https://github.com/doublecloud/python-sdk/commit/dfbc403e47b084199688cb45ddb437a8c75e4287))
* Regenerate for 4.25 ([`aff3358`](https://github.com/doublecloud/python-sdk/commit/aff33580b418ed127d4e6cbd8c0ebffc67dfdd2b))
* Pin protobuf, revert other dependencies changes ([`0bb85eb`](https://github.com/doublecloud/python-sdk/commit/0bb85eb545544895268eab62c365520470585348))
* Build: regenerate proto ([`8a32580`](https://github.com/doublecloud/python-sdk/commit/8a3258076094a355165c910023f7ecc77cab33e4))
* Build: regenerate proto ([`071217a`](https://github.com/doublecloud/python-sdk/commit/071217a2190b974e4b5639295c940bcc73f7e422))
* Build: regenerate proto ([`e8969eb`](https://github.com/doublecloud/python-sdk/commit/e8969ebe3892833c948558c33eb6d1e98681b08b))
* Build: regenerate proto ([`4a3dd2a`](https://github.com/doublecloud/python-sdk/commit/4a3dd2a15d72d05f971b4d1a12f51421218e2f63))
* Build: regenerate proto ([`222fbf4`](https://github.com/doublecloud/python-sdk/commit/222fbf4cd69ff8088f1546552e8a7ca55fca1ab4))
* Build: regenerate proto ([`e71ed2a`](https://github.com/doublecloud/python-sdk/commit/e71ed2a4e4a45aca89663dae307a2a78012f2a82))
* Build: regenerate proto ([`75e4b76`](https://github.com/doublecloud/python-sdk/commit/75e4b76886eda99de96337804264911a051b1a1a))
* Build: regenerate proto ([`7c72fd9`](https://github.com/doublecloud/python-sdk/commit/7c72fd9a68ed1390792fc813426f810e7aed1cf0))

## v0.12.0 (2024-08-08)

### Feature

* Revert "Revert "0.11.0""

This reverts commit bfe4aa2490c9549845948e6f3fbb240cf806c77e. ([`fcca8b3`](https://github.com/doublecloud/python-sdk/commit/fcca8b36cb2c729c2b8840c107e6be4aa8f3952d))
* Revert "0.11.0"

This reverts commit d8eb080af0ed4d0f6710241d4d1364a8c56c0cda. ([`bfe4aa2`](https://github.com/doublecloud/python-sdk/commit/bfe4aa2490c9549845948e6f3fbb240cf806c77e))

## v0.11.0 (2024-08-08)

### Feature

* Better

* upgrade all deps to latest to fix issues with local toolchain
* add exceptions for linters for new generated paths
* tiny rename for buf ([`58b59d5`](https://github.com/doublecloud/python-sdk/commit/58b59d55d298cc85af5ad6fc97dacee92ce2d11d))
* * update buf and pin all dependencies ([`e34b843`](https://github.com/doublecloud/python-sdk/commit/e34b84351d058436fb4202efe5edcf3bbfa42d68))
* Build: regenerate proto ([`6666e51`](https://github.com/doublecloud/python-sdk/commit/6666e515561c67f1f5faeada45654c61c7f4e02d))

## v0.10.0 (2024-07-26)



## v0.9.0 (2024-07-26)

### Feature

* Build: regenerate proto ([`0178456`](https://github.com/doublecloud/python-sdk/commit/0178456337349b0f62aa9c95c48f44e5a70c1633))
* Do not test auto-generated files ([`d2c9af9`](https://github.com/doublecloud/python-sdk/commit/d2c9af923a588211989f242fa15d3ada2dd3887d))
* * feat: use graviton 3 for examples
* feat: add example with kafka topics and user ([`fecae0e`](https://github.com/doublecloud/python-sdk/commit/fecae0ef9a146f116022fe42b83a5d6778c8d5a9))
* * feat: update specs and rebuild stubs
* build: update buf and python3.12 and eliminate python3.8 ([`18dd16f`](https://github.com/doublecloud/python-sdk/commit/18dd16f442c56d016aca6a9ead5b6338de9c46ad))
* DOCS-220 update resource preset generation in example ([`7cd7267`](https://github.com/doublecloud/python-sdk/commit/7cd7267ff2d221bf9722dccc19285cc79e7136c0))
* DOCS-179 Add GCP as a cloud provider option ([`9b8dd25`](https://github.com/doublecloud/python-sdk/commit/9b8dd2554c38ae3a39d2abcf47fb484de391221d))
* Build: regenerate proto ([`03011bc`](https://github.com/doublecloud/python-sdk/commit/03011bc401506594b9d085cdb27b06c5c9f746e5))
* Build: regenerate proto ([`2451518`](https://github.com/doublecloud/python-sdk/commit/2451518f619fe462f1fe8ec9206c9847238847a7))
* Build: regenerate proto ([`b7570da`](https://github.com/doublecloud/python-sdk/commit/b7570dae815657458a0d5b6e37020f71c76d3206))
* Build: regenerate proto ([`0ff5adc`](https://github.com/doublecloud/python-sdk/commit/0ff5adc68564cb7075b71897e5997c85d13273bb))
* Build: regenerate proto ([`068f873`](https://github.com/doublecloud/python-sdk/commit/068f8736990b62892711bf0312e1ade65b8de112))
* Build: regenerate proto ([`fd85f9e`](https://github.com/doublecloud/python-sdk/commit/fd85f9e51f623530accb6cedffbaee248869d42c))

## v0.8.0 (2023-07-17)

### Feature

* Build: pin semantic_release due to unstable 0.8 version ([`4b7a0e6`](https://github.com/doublecloud/python-sdk/commit/4b7a0e68839ab0db14c43eefc079cf52cc15603a))
* Build: regenerate proto ([`77ac47b`](https://github.com/doublecloud/python-sdk/commit/77ac47b0069b46a2359c473c972e5738783b07c6))
* Build: regenerate proto ([`89fc539`](https://github.com/doublecloud/python-sdk/commit/89fc5397d6558ab04470168bcc80634ef207f267))

## v0.7.0 (2023-06-27)

### Feature

* Build: regenerate proto ([`e78a467`](https://github.com/doublecloud/python-sdk/commit/e78a467e8ffe589813b748357b52d06007b16032))

## v0.6.0 (2023-06-13)

### Feature

* Docs: rearrange examples to dedicated files ([`9adbd85`](https://github.com/doublecloud/python-sdk/commit/9adbd856b37f0ae2f5595fab3b9de43475cb95ae))
* Further wording improvements ([`6b0ff0b`](https://github.com/doublecloud/python-sdk/commit/6b0ff0b34b321327965d0c48dc76acaf3593cf60))
* Further wording improvements ([`4f3d68b`](https://github.com/doublecloud/python-sdk/commit/4f3d68beb03757b0b575d51e6713301b0553476c))
* Commit fixes ([`3144604`](https://github.com/doublecloud/python-sdk/commit/31446043431302fceaa44ab62263ac0eaa1f356a))
* Docs: rearrange examples to dedicated files ([`1f46be3`](https://github.com/doublecloud/python-sdk/commit/1f46be3177c934248187c6b10510cbca0faee48f))
* Build: regenerate proto ([`31b47db`](https://github.com/doublecloud/python-sdk/commit/31b47db17f326a670e31ee6e1878f1be722fa77b))
* Build: regenerate proto ([`18a792b`](https://github.com/doublecloud/python-sdk/commit/18a792b6294acf3fd0e280cc0104463ceb1297ee))
* Build: regenerate proto ([`931ef0a`](https://github.com/doublecloud/python-sdk/commit/931ef0a750dc7edc5e34b8aad0b111d2c05c56d8))
* Build: regenerate proto ([`8a60693`](https://github.com/doublecloud/python-sdk/commit/8a606935ab2498b9774702637e074e45e18c9400))
* Build: regenerate proto ([`ed1a49e`](https://github.com/doublecloud/python-sdk/commit/ed1a49e1d25fd84da7307f5fa915767d03dbedeb))
* Docs: add activate example to data transfer ([`8981dfb`](https://github.com/doublecloud/python-sdk/commit/8981dfb47aac4a34e8882830c7d99d54cb585a61))

## v0.5.0 (2023-05-02)
### Feature
* Build: regenerate proto ([`e9a494b`](https://github.com/doublecloud/python-sdk/commit/e9a494b8b59865d9444f40626fa85955d55bde9f))
* Make minor layout changes to improve readability. ([`d3abc79`](https://github.com/doublecloud/python-sdk/commit/d3abc797502410e3b6db58ed8a8e22500b652a0f))
* Add links to relevant documentation articles ([`08cb895`](https://github.com/doublecloud/python-sdk/commit/08cb895b750ed0188db524c74784581e8752c38b))

## v0.4.0 (2023-04-13)
### Feature
* Build: add pyi files into python package ([`bbfd5c4`](https://github.com/doublecloud/python-sdk/commit/bbfd5c4d01d227f40fb6906c1f0b99cc316ca2f0))

## v0.3.0 (2023-04-13)
### Feature
* Feat: add pyi files for working with type hinting 🦆 ([`3923355`](https://github.com/doublecloud/python-sdk/commit/392335512f9d285b16fb738eea21512c1cf45d8a))
* Docs: Add example for DoubleCloud Visualization

  * wait a pressed key for deleting examples 🫡
  * use commit msg convetion for ci builds
  * lint forgotten {setup,changelog}.py ([`fea5c95`](https://github.com/doublecloud/python-sdk/commit/fea5c9529dd49eb175f57607b00acdaf7b196e49))
* Regenerate proto ([`59fd5f6`](https://github.com/doublecloud/python-sdk/commit/59fd5f6d7ba8d66c4bd8fb4ee30ce1488a7dc571))
* Ci: set token for github-action/regenerate step

* Forward github token for pushing changed generated code ([`6e1dd99`](https://github.com/doublecloud/python-sdk/commit/6e1dd99f8d9a85c38428a628daf442d3d0d9ec66))
* Update readme ([`ba0f85c`](https://github.com/doublecloud/python-sdk/commit/ba0f85c0cb955c010b7afa54629c8d5cb1949590))
* Ci: fix github actions

* Eliminate github token forwarding after publishing.
* Fix protobuf spec generation misspell ([`95a17e7`](https://github.com/doublecloud/python-sdk/commit/95a17e7dd354601bf55b71d7c7d8bfba45372165))

## v0.2.0 (2023-03-31)
### Feature
* Build: tidy up ([`0915489`](https://github.com/doublecloud/python-sdk/commit/0915489b94234c9241cb2904c90a6c79fe683fc7))

## v0.1.0 (2023-03-31)
### Feature
* Feat: Double.Cloud: Hello, world! 🚀 ([`a501a06`](https://github.com/doublecloud/python-sdk/commit/a501a065cf9715cb564a88de792951125fbd3300))
