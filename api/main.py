from fastapi import FastAPI
from utils.blockchain import pay_money
from pydantic import BaseModel  # Import BaseModel for defining request/response models

app = FastAPI()

class TransactionReceipt(BaseModel):
    transaction_hash: str
    # Add other attributes from the tx_receipt that you want to expose in the API response

@app.post('/api/pay_money', response_model=TransactionReceipt)
def invoke_pay_money(amt: int):
    try:
        tx_receipt = pay_money(amt)
        # Extract relevant attributes from tx_receipt and return as JSON-serializable response
        response_data = {
            'transaction_hash': tx_receipt.transactionHash.hex(),
            # Add other attributes as needed
        }
        return response_data
    except Exception as e:
        return {'error': str(e)}
