from typing import Any

from clickhouse_sqlalchemy.ext.declarative import ClickHouseDeclarativeMeta


class Base(ClickHouseDeclarativeMeta):
    id: Any
    __name__: str

    __allow_unmapped = True

    def __tablename__(cls):
        return cls.__name__.lower()
