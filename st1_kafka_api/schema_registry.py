import json
from requests import Response
from .requester import Requester


class SchemaRegistry(Requester):

    async def create_schema(self, name: str, schema: dict) -> Response:
        return await self.make_request('POST', '/subjects/' + name + '/versions',
            json = { 'schema': json.dumps(schema) })

