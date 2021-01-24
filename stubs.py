# stubs for main.py
class DenoNameSpace:
    env: {}

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


class JSONClass:
    def parse(self, text):
        return {}

    def stringify(self, obj):
        return "{}"


JSON = JSONClass()
