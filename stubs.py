# stubs for main.py
class DenoNameSpace:
    env = {}

    def readTextFileSync(self, name):
        return ""


Deno = DenoNameSpace()


class Response:
    status = 200

    async def json(self):
        return {}

    async def text(self):
        return ""


def fetch(url):
    return Response()


class JSON:
    @classmethod
    def parse(cls, text):
        return {}

    @classmethod
    def stringify(cls, obj):
        return "{}"


# Lodash
class Lodash:
    def camelCase(self, text):
        return ""


lodash = Lodash()
