import aiosqlite
from pathlib import Path


class User:
    def __init__(self, db_path):
        self.db_path = db_path


    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"CREATE TABLE IF NOT EXISTS users "
                f"([id] INTEGER PRIMARY KEY AUTOINCREMENT, "
                f"[telegram_id] INTEGER UNIQUE NOT NULL, "
                f"[active] BOOLEAN DEFAULT (TRUE))"
            )
            await db.commit()


    async def add_user(self, telegram_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"INSERT INTO users(telegram_id) VALUES ({telegram_id})"
            )
            await db.commit()


    async def user_existing(self, telegram_id: int) -> bool:
        async with aiosqlite.connect(self.db_path) as db:
            res = await db.execute_fetchall(
                f"SELECT * FROM users WHERE telegram_id = {telegram_id}"
            )
            return bool(res)