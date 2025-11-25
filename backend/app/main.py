from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio

from backend.app.database import get_db, engine
from backend.app.models import Base, Transaction, TransactionStatus, User
from backend.app.escrow import EscrowContract
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

class P2PSwapRequest(BaseModel):
    sender: str
    receiver: str
    amount: float

escrow_contract = EscrowContract(contract_address="sample_contract_address")

async def get_current_user():
    # This will be replaced by Telegram WebApp API identity logic
    return {"username": "test_user"}

@app.post("/p2p/swap")
async def create_p2p_swap(swap: P2PSwapRequest, user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    # Call escrow contract initiate_swap
    txn_hash = escrow_contract.initiate_swap(sender_wallet=swap.sender, receiver_wallet=swap.receiver, amount=swap.amount)

    # Fetch sender and receiver users or create if not exist
    sender_user = await db.execute(
        User.__table__.select().where(User.telegram_username == swap.sender)
    )
    sender_user = sender_user.scalars().first()
    if not sender_user:
        sender_user = User(telegram_username=swap.sender)
        db.add(sender_user)
        await db.commit()
        await db.refresh(sender_user)

    receiver_user = await db.execute(
        User.__table__.select().where(User.telegram_username == swap.receiver)
    )
    receiver_user = receiver_user.scalars().first()
    if not receiver_user:
        receiver_user = User(telegram_username=swap.receiver)
        db.add(receiver_user)
        await db.commit()
        await db.refresh(receiver_user)

    # Create transaction record
    transaction = Transaction(
        sender_id=sender_user.id,
        receiver_id=receiver_user.id,
        amount=swap.amount,
        status=TransactionStatus.pending,
        escrow_contract_txn=txn_hash
    )
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)

    return {
        "message": "P2P swap initiated",
        "transaction_id": transaction.id,
        "escrow_txn_hash": txn_hash

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

# Dummy dependency stub for user authentication to be expanded
def get_current_user():
    # This will be replaced by Telegram WebApp API identity logic
    return {"username": "test_user"}

class P2PSwapRequest(BaseModel):
    sender: str
    receiver: str
    amount: float

class MerchantQRRequest(BaseModel):
    merchant_id: str
    amount: float

@app.get("/")
def read_root():
    return {"status": "backend running"}

@app.post("/p2p/swap")
def create_p2p_swap(swap: P2PSwapRequest, user=Depends(get_current_user)):
    # TODO: Integrate with escrow contract and database
    return {
        "message": "P2P swap request received",
        "details": swap.dict(),
        "user": user
    }

@app.post("/merchant/qr")
def generate_merchant_qr(data: MerchantQRRequest, user=Depends(get_current_user)):
    # TODO: Generate QR for merchant payment and return QR code data
    return {
        "message": "Merchant QR generation request received",
        "details": data.dict(),
        "user": user
    }

from backend.app.telegram_auth import verify_telegram_auth
from fastapi import Request

@app.post("/telegram/auth")
async def telegram_auth(request: Request):
    auth_data = await request.json()
    user_info = verify_telegram_auth(auth_data)
    # TODO: Create user session or JWT token based on verified user_info
    return {
        "message": "Telegram auth verified successfully",
        "user_info": user_info
    }
