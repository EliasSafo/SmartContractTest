from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.blockchain import pay_money  # Import the pay_money function from your utils/blockchain.py

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PaymentRequest(BaseModel):
    sender: str
    receiver: str
    amt: int


class TransactionReceipt(BaseModel):
    transaction_hash: str
    # Add other attributes from the tx_receipt that you want to expose in the API response


@app.post('/api/pay_money', response_model=TransactionReceipt)
async def invoke_pay_money(payment_request: PaymentRequest):
    try:
        sender_account = payment_request.sender
        receiver_account = payment_request.receiver
        amt = payment_request.amt
        tx_receipt = pay_money(sender_account, receiver_account, amt)
        # Extract relevant attributes from tx_receipt and return as JSON-serializable response
        response_data = {
            'transaction_hash': tx_receipt.transactionHash.hex(),
            # Add other attributes as needed
        }
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
