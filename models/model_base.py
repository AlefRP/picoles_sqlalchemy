import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

Base = declarative_base()

class ModelBase(Base):
    __abstract__ = True  # Define a classe como abstrata

    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(sa.Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def data_criacao(cls) -> Mapped[datetime]:
        return mapped_column(sa.DateTime, default=datetime.utcnow, index=True)
