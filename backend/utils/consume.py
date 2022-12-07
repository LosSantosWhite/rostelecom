import asyncio
import json

import aio_pika
from aio_pika import connect_robust
from aio_pika.patterns import RPC

from servicedb.utils import create_appeal
from servicedb.db import engine
from sqlalchemy.orm import Session


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        session = Session(engine)
        data = json.loads(message.body)
        with session.begin():
            create_appeal(data, session)


async def consume(loop):
    connection = await connect_robust("amqp://guest:guest@rabbitmq", loop=loop)
    channel = await connection.channel()
    rpc = await RPC.create(channel)
    await rpc.register("process_message", process_message)
    queue_name = "appeals"
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=100)
    queue = await channel.declare_queue(queue_name)
    await queue.consume(process_message)
    try:
        await asyncio.Future()
    finally:
        await connection.close()
    return connection
