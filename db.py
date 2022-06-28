import aiosqlite


class User:
    def __init__(self, db_path):
        self.db_path = db_path


    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"CREATE TABLE IF NOT EXISTS users "
                f"([id] INTEGER PRIMARY KEY AUTOINCREMENT, "
                f"[telegram_id] INTEGER UNIQUE NOT NULL, "
                f"[active] BOOLEAN DEFAULT (TRUE),"
                f"[branch] TEXT)"
            )
            await db.commit()


    async def add_user(self, telegram_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"INSERT INTO users(telegram_id, branch) VALUES ({telegram_id}, '')"
            )
            await db.commit()


    async def user_existing(self, telegram_id: int) -> bool:
        async with aiosqlite.connect(self.db_path) as db:
            res = await db.execute_fetchall(
                f"SELECT * FROM users WHERE telegram_id = {telegram_id}"
            )
            return bool(res)


    async def update_user_branch(self, telegram_id: int, branch: str):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"UPDATE users SET branch = '{branch}' WHERE telegram_id = {telegram_id}"
            )
            await db.commit()


    async def get_user_branch(self, telegram_id: int) -> str:
        async with aiosqlite.connect(self.db_path) as db:
            res = await db.execute_fetchall(
                f"SELECT branch FROM users WHERE telegram_id = {telegram_id}"
            )
            return res