from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Account
account = w3.eth.accounts[0]

# Contract Address (👉 COPY from Ganache → Transactions)
contract_address = "0x773126232EF5616992aF91da12984C6092E81788"

# Load ABI
with open("blockchain/build/contracts/FileStorage.json") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

# Contract Instance
contract = w3.eth.contract(address=contract_address, abi=abi)