<div align="right">

  [![license](https://img.shields.io/github/license/block-foundation/teal-houding-cooperative?color=green&label=license&style=flat-square)](LICENSE.md)
  ![stars](https://img.shields.io/github/stars/block-foundation/teal-houding-cooperative?color=blue&label=stars&style=flat-square)
  ![contributors](https://img.shields.io/github/contributors/block-foundation/teal-houding-cooperative?color=blue&label=contributors&style=flat-square)

</div>

---

<div>
    <img align="right" src="https://raw.githubusercontent.com/block-foundation/brand/master/logo/logo_gray.png" width="96" alt="Block Foundation Logo">
    <h1 align="left">Blockchain Housing Cooperative Management</h1>
    <h3 align="left">Block Foundation Smart Contract Series [Teal]</h3>
</div>

---

<div>
<img align="right" width="75%" src="https://raw.githubusercontent.com/block-foundation/brand/master/image/repository_cover/block_foundation-structure-03-accent.jpg"  alt="Block Foundation">
<br>
<details open="open">
<summary>Table of Contents</summary>
  
- [Introduction](#style-guide)
- [Quick Start](#quick-start)
- [Contract](#contract)
- [Development Resources](#development-resources)
- [Legal Information](#legal-information)
  - [Copyright](#copyright)
  - [License](#license)
  - [Warning](#warning)
  - [Disclaimer](#disclaimer)

</details>
</div>

<br clear="both"/>

## Introduction

Welcome to Blockchain Housing Cooperative Management! This project aims to leverage blockchain technology to provide an efficient, transparent, and secure platform for managing housing cooperatives.

Traditionally, housing cooperatives have faced challenges in areas such as record keeping, transparency, property ownership transfer, and fund management. Our project addresses these challenges by harnessing the power of blockchain technology. We are creating a decentralized application (DApp) that will maintain a record of all houses owned by the cooperative, track the owners of each house, and handle transactions related to these properties, all in a secure and transparent manner.

This platform will use smart contracts - self-executing contracts with the terms of the agreement directly written into code. For our project, we'll be using Solidity for Ethereum blockchain and PyTeal for Algorand blockchain. These smart contracts will handle tasks such as adding new houses to the cooperative, changing ownership, and managing funds for house purchases.

Our project will offer benefits like improved transparency, as every transaction will be recorded on the blockchain and can be audited. It will also increase efficiency, as transactions and changes of ownership can be handled within the blockchain without the need for a middleman. Lastly, it ensures higher security and trust as the blockchain ledger is immutable and every transaction can be traced and verified.

The end goal of this project is to revolutionize how housing cooperatives are managed, by bringing them into the digital age and making them more secure, efficient, and transparent. Whether you are part of a housing cooperative, interested in the potential of blockchain technology, or just curious to see how decentralized applications can be used in new and exciting ways, we invite you to join us on this journey of innovation.

Welcome aboard! Let's build the future of housing cooperatives together.

## Quick Start


## Contract

This program stores a `house` as a Local state (associated with the sender's address) and the `creator` (the contract creator) as a Global state. Only the `creator` can set the owner of the house or add a house to the ledger.


## Development Resources

### Other Repositories

#### Block Foundation Smart Contract Series

|                                   | `Solidity`  | `Teal`      |
| --------------------------------- | ----------- | ----------- |
| **Template**                      | [**>>>**](https://github.com/block-foundation/solidity-template) | [**>>>**](https://github.com/block-foundation/teal-template) |
| **Architectural Design**          | [**>>>**](https://github.com/block-foundation/solidity-architectural-design) | [**>>>**](https://github.com/block-foundation/teal-architectural-design) |
| **Architecture Competition**      | [**>>>**](https://github.com/block-foundation/solidity-architecture-competition) | [**>>>**](https://github.com/block-foundation/teal-architecture-competition) |
| **Housing Cooporative**           | [**>>>**](https://github.com/block-foundation/solidity-housing-cooperative) | [**>>>**](https://github.com/block-foundation/teal-housing-cooperative) |
| **Land Registry**                 | [**>>>**](https://github.com/block-foundation/solidity-land-registry) | [**>>>**](https://github.com/block-foundation/teal-land-registry) |
| **Real-Estate Crowdfunding**      | [**>>>**](https://github.com/block-foundation/solidity-real-estate-crowdfunding) | [**>>>**](https://github.com/block-foundation/teal-real-estate-crowdfunding) |
| **Rent-to-Own**                   | [**>>>**](https://github.com/block-foundation/solidity-rent-to-own) | [**>>>**](https://github.com/block-foundation/teal-rent-to-own) |
| **Self-Owning Building**          | [**>>>**](https://github.com/block-foundation/solidity-self-owning-building) | [**>>>**](https://github.com/block-foundation/teal-self-owning-building) |
| **Smart Home**                    | [**>>>**](https://github.com/block-foundation/solidity-smart-home) | [**>>>**](https://github.com/block-foundation/teal-smart-home) |

## Legal Information

### Copyright

Copyright 2023, [Stichting Block Foundation](https://www.blockfoundation.io). All rights reserved.

### License

Except as otherwise noted, the content in this repository is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/), and
code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).

Also see [LICENSE](https://github.com/block-foundation/community/blob/master/LICENSE) and [LICENSE-CODE](https://github.com/block-foundation/community/blob/master/LICENSE-CODE).

### Warning

**Please note that this code should be audited by a professional smart-contract auditor before being used in a production environment as it is a simplified example and may not cover all potential security vulnerabilities.**

### Disclaimer

**THIS SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
