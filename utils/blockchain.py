# utils/blockchain.py
import os
from web3 import Web3
import json


def pay_money(amt: int):
    # Connect to Ganache
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Set the default account (from Ganache) for transactions
    web3.eth.default_account = web3.eth.accounts[0]

    # Resolve the path to SimpleStorage.json dynamically
    contract_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'build', 'contracts', 'SimpleStorage.json')
    )

    # Load contract ABI and address
    with open(contract_file_path) as f:
        contract_data = json.load(f)
        abi = contract_data['abi']
        contract_address = "0x9f04F76CB09A6aDc2c1765e0e19248e45397044f"  # Contract address

    # Create contract instance
    contract = web3.eth.contract(address=contract_address, abi=abi)
    sender_account = web3.eth.accounts[0]
    receiver_account = web3.eth.accounts[1]

    # Prepare transaction parameters
    transaction_params = {
        'from': sender_account,
        'value': web3.to_wei(amt, 'ether'),  # Amount of ether (1 ETH in wei) to send with the transaction
        'gas': 200000,  # Gas limit for the transaction
    }

    # Call the payMoney() function by sending a transaction
    tx_hash = contract.functions.payMoney(receiver_account).transact(transaction_params)

    # Wait for transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    # Return transaction receipt
    return tx_receipt
