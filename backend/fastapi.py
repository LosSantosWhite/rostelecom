import asyncio

import fastapi

from servicedb import models
from servicedb.db import engine, SessionLocal
from backend.utils import consume


models.Base.metadata.create_all(bind=engine)


app = fastapi.FastAPI()


@app.on_event("startup")
def start_loop():
    print("starting app")
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(consume.consume(loop))
