from clickhouse_sqlalchemy.ext.declarative import ClickHouseDeclarativeMeta


class Base(metaclass=ClickHouseDeclarativeMeta):
    __abstract__ = True

    @classmethod
    def __tablename__(cls):
        return cls.__name__.lower()
