def __pragma__(directive: str, *args) -> str:
    return ""


# stubs for main.py
class DenoNameSpace:
    env: dict = {}

    def readTextFileSync(self, name) -> str:
        return ""


Deno = DenoNameSpace()


class Response:
    status = 200

    async def json(self) -> dict:
        return {}

    async def text(self) -> str:
        return ""


def fetch(url) -> Response:
    return Response()


class JSON:
    @classmethod
    def parse(cls, text) -> dict:
        return {}

    @classmethod
    def stringify(cls, obj) -> str:
        return "{}"


# Lodash
class Lodash:
    def camelCase(self, text: str) -> str:
        return ""


lodash = Lodash()
