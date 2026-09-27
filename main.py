import asyncio
import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import settings
from models import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

logging.basicConfig(level=logging.INFO)

# Инициализация БД
engine = create_async_engine(settings.DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Инициализация Бота и FastAPI
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
app = FastAPI(title="Casiubrot Casino API")

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Заменишь URL на ссылку с хостинга, когда запустим Render
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 Играть в Casiubrot", web_app=WebAppInfo(url="https://google.com"))]
    ])
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"👑 Добро пожаловать в **Casiubrot Casino**!\n"
        f"Жми кнопку ниже и забирай свой стартовый бонус!",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "app": "Casiubrot Casino"}

async def start_bot():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await dp.start_polling(bot)

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(start_bot())
