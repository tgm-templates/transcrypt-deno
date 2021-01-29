import json


def __pragma__(directive: str, *args) -> str:
    return ""


def __new__(obj):
    return obj


# stubs for main.py
class DenoNameSpace:
    env: dict = {}

    def readTextFileSync(self, name) -> str:
        return ""


Deno = DenoNameSpace()


class Response:
    status = 200

    def __init__(self, body, headers: dict) -> None:
        pass

    async def json(self) -> dict:
        return {}

    async def text(self) -> str:
        return ""


def fetch(url) -> Response:
    return Response("", {})


class JSON:
    @classmethod
    def parse(cls, text) -> dict:
        return json.loads(text)

    @classmethod
    def stringify(cls, obj) -> str:
        return json.dumps(obj)


# Lodash
class Lodash:
    def camelCase(self, text: str) -> str:
        return ""


lodash = Lodash()
