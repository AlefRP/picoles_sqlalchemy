import sqlalchemy as sa
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class Revendedor(ModelBase):
    __tablename__ = 'revendedores'
    
    ativo: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    cnpj: Mapped[str] = mapped_column(sa.String(14), unique=True, nullable=False)
    razao_social: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)
    contato: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Revendedor: {self.razao_social}>'
