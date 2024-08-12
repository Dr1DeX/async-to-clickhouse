from sqlalchemy.orm import registry

_registry = registry()


class Base(_registry.generate_base()):
    __abstract__ = True

    @classmethod
    def __tablename__(cls):
        return cls.__name__.lower()
