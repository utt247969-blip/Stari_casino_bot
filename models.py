from datetime import datetime
from sqlalchemy import BigInteger, String, Float, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    
    balance_stars: Mapped[float] = mapped_column(Float, default=100.0)
    safe_balance_stars: Mapped[float] = mapped_column(Float, default=0.0)
    
    is_vip: Mapped[bool] = mapped_column(Boolean, default=False)
    level: Mapped[int] = mapped_column(Integer, default=1)
    xp: Mapped[int] = mapped_column(Integer, default=0)
    total_wager: Mapped[float] = mapped_column(Float, default=0.0)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="completed")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)