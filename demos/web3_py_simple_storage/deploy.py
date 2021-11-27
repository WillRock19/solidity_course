# importing package solcx as solidity compiler
from solcx import compile_standard, install_solc
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

# Now that we have our bytecode and out ABI, we need to deploy it. We could deploy into an existing blockchain, but, for the
# sole pourposes of study, we are going to use an local blockchain. For that, we are going to use GANACHE. It's going to be
# our local deploy blockchain. basically, it's going to act as our Javascript VM (which we use in the remix site)
