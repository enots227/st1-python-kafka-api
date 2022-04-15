import json
from typing import Union
from asgiref.sync import sync_to_async
from urllib.parse import urljoin
import logging
import requests


logger = logging.getLogger(__name__)


class Requester:

    def __init__(self, url: str):
        self.url = url

    def _url(self, path: str) -> str:
        return urljoin(self.url, path)

    @sync_to_async
    def make_request(self,
        method: Union[str,bytes],
        path: Union[str,bytes],
        **kwargs
    ) -> requests.Response:
        url = self._url(path)
        
        payload = kwargs['json'] if 'json' in kwargs else None
        
        logger.info('kafka API request', extra={ 'method': method, 'url': url,
            'payload': payload })
            
        resp = requests.request(method, url, **kwargs)

        content = resp.content.decode('UTF-8')

        try:
            content = json.loads(content)
        except ValueError:
            logger.debug('kafka API response - is not JSON')

        logger.info('kafka API response', extra={ 'method': method, 'url': url,
            'content': content })

        return resp

