import asyncio
import aio_pika
from aio_pika import connect_robust
from aio_pika.patterns import RPC


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        print(message.body)
        # запись в бд
        await asyncio.sleep(1)


async def consume(loop):
    connection = await connect_robust("amqp://guest:guest@rabbitmq/", loop=loop)
    channel = await connection.channel()
    rpc = await RPC.create(channel)

    # Register your remote method
    await rpc.register("process_message", process_message)
    queue_name = "appeals"

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(queue_name)

    await queue.consume(process_message)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()
    return connection
