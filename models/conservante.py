import sqlalchemy as sa
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class Conservante(ModelBase):
    __tablename__ = 'conservantes'
    
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Conservante: {self.nome}>'
