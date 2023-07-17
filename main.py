import asyncio
import uvicorn
from fastapi import FastAPI

from api.api import router
from bd.database import sqlite_db_init

app = FastAPI()

app.include_router(router)

async def main():
    """
    Главная асинхронная функция, которая инициализирует базу данных и запускает сервер FastAPI.
    """
    await sqlite_db_init()
    uvicorn_config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(uvicorn_config)
    loop = asyncio.get_event_loop()
    loop.create_task(server.serve())
    try:
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass
    finally:
        server.should_exit = True

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
