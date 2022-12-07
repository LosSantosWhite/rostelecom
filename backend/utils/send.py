from aio_pika import Message, connect
import asyncio


async def send_message(message):
    # отправка обращения в очередь
    connection = await connect("amqp://guest:guest@rabbitmq/")

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("appeals")

        await channel.default_exchange.publish(Message(message), routing_key=queue.name)
