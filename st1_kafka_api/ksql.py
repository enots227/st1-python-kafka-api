from requests import Response
from .requester import Requester


class KSQL(Requester):

    async def execute(self, ksql: str) -> Response:
        return await self.make_request('POST', '/ksql', json={ 'ksql': ksql })

    async def query(self, ksql: str) -> Response:
        return await self.make_request('POST', '/query', json={ 'ksql': ksql })
