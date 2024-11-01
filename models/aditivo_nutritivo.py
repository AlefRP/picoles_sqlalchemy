import sqlalchemy as sa
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class AditivoNutritivo(ModelBase):
    __tablename__ = 'aditivos_nutritivos'
    
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    formula_quimica: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Aditivo Nutritivo: {self.nome}>'
