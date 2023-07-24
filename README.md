# teal-housing-cooperative


PyTeal is a high-level language for writing smart contracts on the Algorand blockchain. The language constructs are different from Solidity, which is used on the Ethereum blockchain. Also, Algorand's smart contracts are currently less expressive than Ethereum's in terms of complex state manipulations. Thus, we might not be able to perfectly translate the Solidity contract into PyTeal due to the inherent differences between these two platforms.

Below is a basic example that tries to represent the previous contract, but some features like the ability to put a house for sale or to buy a house cannot be expressed with the same level of complexity in PyTeal as in Solidity as of my knowledge cutoff in September 2021.



This program stores a "house" as a Local state (associated with the sender's address) and the "creator" (the contract creator) as a Global state. Only the "creator" can set the owner of the house or add a house to the ledger.

Please remember that this is a simplified version of a Housing Cooperative contract and may not cover all your needs. You should reach out to a professional who is well-versed with PyTeal and Algorand to help create a more comprehensive and secure contract.