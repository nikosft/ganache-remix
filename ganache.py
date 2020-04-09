from web3 import Web3
import json

bin_file = "YOUR_BYTECODE_FILE"
ABI_file = "YOUR_ABI_FILE"

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
with open(ABI_file, 'r') as myfile:
  abi = myfile.read()

with open(bin_file, 'r') as myfile:
  binfile = myfile.read()
  bytecode = json.loads(binfile)['object']

account = w3.eth.accounts[0]
MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = MyContract.constructor().transact({'from': account})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
address = tx_receipt.contractAddress
print(address)