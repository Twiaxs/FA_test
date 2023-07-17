from tortoise import Tortoise


MODELS_LIST = ["models.models"]

async def sqlite_db_init() -> None:
    """
    Инициализация базы данных SQLite с помощью Tortoise ORM.
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={'models': MODELS_LIST}
    )

    await Tortoise.generate_schemas()


