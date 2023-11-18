# Introduction to Blockchain and Node Providers

This is a Github repository to help newcomers to the blockchain space get access to on-chain data and learn more about how to interact with smart contracts and nodes. This first version accompanies the technical workshop "Intro to Blockchain and On-chain Data" at Mhacks 2023 at the University of Michigan organized by V1 Michigan.

Here's a link to the slides for the workshop: [Workshop: Intro to Blockchain and On-chain Data](https://www.canva.com/design/DAF0iPhhpHg/Dly1oq2yrK_Z9YAHiUz00Q/view?utm_content=DAF0iPhhpHg&utm_campaign=designshare&utm_medium=link&utm_source=editor)


## What is Blockchain?

Blockchain is a decentralized, distributed ledger technology that records transactions in a secure and immutable way. It underpins cryptocurrencies like Bitcoin and Ethereum but also has a wide range of applications beyond cryptocurrencies.

## Connecting to a Blockchain Node

To interact with a blockchain, one needs to connect to a blockchain node. A node is an instance of the data structure which makes up the blockchain itself. You can run your own node or connect to existing nodes provided by third-party services like Infura, Alchemy, and Quicknode.

## Infura

Infura provides instant access to the Ethereum and IPFS networks through its API. It's widely used for deploying smart contracts, sending transactions, and querying blockchain data.

- **Documentation**: [Infura Documentation](https://infura.io/docs)

## Alchemy

Alchemy is a blockchain developer platform that provides tools and APIs for building, debugging, and scaling blockchain applications. It supports Ethereum, Polygon, Arbitrum, and more.

- **Documentation**: [Alchemy Documentation](https://docs.alchemy.com/alchemy/)

## Quicknode

Quicknode accelerates blockchain development by providing high-performance node infrastructure. It supports multiple blockchains, including Ethereum, Bitcoin, and Solana.

- **Documentation**: [Quicknode Documentation](https://www.quicknode.com/docs)

## The Graph

The Graph is a decentralized protocol for indexing and querying blockchain data. Developers can build and publish open APIs, called subgraphs, that applications can query using GraphQL.

- **Documentation**: [The Graph Documentation](https://thegraph.com/docs/en/)

## Etherscan: Viewing Blockchain Data Without Coding

Etherscan is a Block Explorer and Analytics Platform for Ethereum, allowing you to view transaction data, wallet addresses, and smart contract information on the Ethereum blockchain without writing any code.

- **Website**: [Etherscan](https://etherscan.io/)

## Getting On-Chain Data Programmatically

Using the services mentioned above, developers can programmatically interact with blockchain networks. Infura, Alchemy, and Quicknode provide APIs to connect to nodes, while The Graph allows for querying blockchain data efficiently.

## Running the Utility Scripts

In this repository, we have two utility scripts located in the `utils` directory:

1. `get_latest_block.py` - Retrieves the latest block number from the Ethereum blockchain.
2. `get_token_balance.py` - Fetches the ERC-20 token balance for a specified wallet address.

### Prerequisites

Before running these scripts, ensure you have Python installed on your system and the `web3` Python package installed. You can install `web3` using pip:

`pip install web3`

This is also in our `requirements.txt` so you can also create a virtual environment and install all of the dependencies with these commands:

`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`

If you have any other dependencies, feel free to install them and freeze them as well with `pip freeze > requirements.txt`

Additionally, as we are using Infura for these example functions, you should create a free account and replace the `` with your URL with your key. Remember to keep these keys secret in your actual products and NEVER push these URL strings/keys to Github repositories
