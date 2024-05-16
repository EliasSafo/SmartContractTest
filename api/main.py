from utils.blockchain import pay_money
from pydantic import BaseModel  # Import BaseModel for defining request/response modelsfrom fastapi import FastAPI, HTTPException
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL(s)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class PaymentRequest(BaseModel):
    amt: int

class TransactionReceipt(BaseModel):
    transaction_hash: str
    # Add other attributes from the tx_receipt that you want to expose in the API response

@app.post('/api/pay_money', response_model=TransactionReceipt)
def invoke_pay_money(payment_request: PaymentRequest):
    try:
        amt = payment_request.amt
        tx_receipt = pay_money(amt)
        # Extract relevant attributes from tx_receipt and return as JSON-serializable response
        response_data = {
            'transaction_hash': tx_receipt.transactionHash.hex(),
            # Add other attributes as needed
        }
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
