# Introduction

This project has some notes and informations about creating a deploy file, in Python, to a .sol script. Here we compile the .sol, create connection to a Blockchain and then deploy our ABI file into it. There are a lot of notes inside the `deploy.py` file so we can understand each step of this process.

When I first tried this out, there where some problems in the configuration (problems with the solcx library, basically). I've added a link to a stackoverflow post that might help, but, to be honest, I don't quite remember if this is enought to resolve all the problems.

If it's not, please feel free to add more information in this notes :)

# Libraries used

### SolcX

* Reason:   Our solidity compiler. We use it so we can compile our .sol files
* Install:  `pip install py-solc-x`
* Notes:    It may occur errors in the installation If it does, check [this link](https://ethereum.stackexchange.com/questions/110405/having-a-problem-with-solc-x-version-solc-0-6-0-has-not-been-installed)

### Web3

* Reason:   Allow us to work with the web3, connecting to a Blockchain and creating transactions.
* Install:  `pip install web3`


### DotEnv

* Reason: read environment variables from a local .env file
* Install: `pip install python-dotenv`

