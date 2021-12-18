# importing package solcx as solidity compiler
from solcx import compile_standard, install_solc
from web3 import Web3
import json

# getting all the code from our SimpleStorage.sol and saving it in a variable
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

# running the installation of solc
install_solc("0.6.0")

# compiling our solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

# save the compiled code (which has our ABI file and our bytecode) into a json file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode walking through every of the json property from the roo until reach our bytecode object
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get the ABI (our contract's interface)
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Now that we have our bytecode and our ABI, we need to deploy it. We could deploy into an existing blockchain (testnet) but, for
# the sole pourposes of study, we are going to use an local blockchain. For that, we are going to use GANACHE. It's going to be
# our local blockchain and it's basically going to act as our Javascript VM (which we use in the remix site).

# connecting to ganache (with rpc server)
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x2db7F5CFD87e7023cf71B69fBF3408f7076099Da"

# adding a fake ganache private key to make our tests
address_private_key = "0x8285a49cdbb4dcdee9273e8a3096a007f1112e6a04c2f103bc70b3296701e52e"  # when adding the private key in python, I allways have to use the 0x sintax as predicate (python will allways look for hex values)

# create the contract with web3's python library (associating it to the ABI and BYTECODE)
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)

# Now, let's think about deploying properly. Whenever we make a state change on blockchain, we need to make a transaction. The deploy is a state change.
# So, to make our deploy, we need to follow three steps:
#
#   1. build the contract deploy transaction;
#   2. sign the transaction;
#   3. send the transaction;
#
# To make a transaction, we need a nonce. The nonce is a one-time use word that can be used in cryptography. We can use the transaction's
# count as the nonce, so it'll always be unique during our contract's lifetime.

# Get latest transaction number
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# Building the transaction. Event that, in our file, we doesn't have a constructor, EVERY contract has one (like objects).
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chain_id": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
print(transaction)

# Now, we need to sign the transaction. Since we are doing from our address, our private key is the only that will work to sign it
signed_txt = w3.eth.account.sign_transaction(transaction, address_private_key)
