import sqlalchemy as sa
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class Sabor(ModelBase):
    __tablename__ = 'sabores'
    
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Sabor: {self.nome}>'
