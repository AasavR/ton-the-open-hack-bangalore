from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_username = Column(String, unique=True, index=True, nullable=False)
    wallet_address = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    transactions_sent = relationship('Transaction', foreign_keys='Transaction.sender_id', back_populates='sender')
    transactions_received = relationship('Transaction', foreign_keys='Transaction.receiver_id', back_populates='receiver')

class Merchant(Base):
    __tablename__ = 'merchants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    telegram_username = Column(String, unique=True, index=True, nullable=False)
    wallet_address = Column(String, unique=True, index=True, nullable=True)
    subscription_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class TransactionStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    disputed = "disputed"
    cancelled = "cancelled"

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.pending)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    escrow_contract_txn = Column(String, nullable=True)  # Txn hash on TON blockchain

    sender = relationship('User', foreign_keys=[sender_id], back_populates='transactions_sent')
    receiver = relationship('User', foreign_keys=[receiver_id], back_populates='transactions_received')

class DisputeStatus(enum.Enum):
    open = "open"
    resolved = "resolved"
    rejected = "rejected"

class Dispute(Base):
    __tablename__ = 'disputes'
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'), nullable=False)
    complainant_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(DisputeStatus), default=DisputeStatus.open)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    transaction = relationship('Transaction', backref='disputes')
    complainant = relationship('User', foreign_keys=[complainant_id])
