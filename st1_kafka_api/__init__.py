from .connect import Connect
from .ksql import KSQL
from .schema_registry import SchemaRegistry


class KafkaAPI:

    def __init__(self,
        bootstrap_servers: str = '',
        client_id: str|None=None,
        connect: Connect=None,
        ksql: KSQL=None,
        schema_registry: SchemaRegistry=None
    ):
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id
        self.connect = connect
        self.ksql = ksql
        self.schema_registry = schema_registry

