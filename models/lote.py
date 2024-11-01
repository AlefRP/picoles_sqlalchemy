import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
from sqlalchemy.orm import Mapped, mapped_column

class Lote(ModelBase):
    __tablename__ = 'lotes'
    
    id_tipo_picole: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined')
    
    quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Lote: {self.id}>'