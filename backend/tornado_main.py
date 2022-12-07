import asyncio

from utils.send import send_message

import tornado.web


class HandleForm(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Max-Age", 1000)
        self.set_header("Content-type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header(
            "Access-Control-Allow-Headers",
            "Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods",
        )

    def options(self):
        pass

    async def post(self):
        try:
            print(self.request.body)
            await send_message(self.request.body)
        except Exception as err:
            print(err)


def make_app():
    return tornado.web.Application(
        [
            (r"/api/user/appeal/", HandleForm),
        ]
    )


async def main():
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
