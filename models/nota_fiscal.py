import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

# Tabela de associação para a relação muitos-para-muitos entre NotaFiscal e Lote
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'))
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'
    
    valor: Mapped[float] = mapped_column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    
    id_revendedor: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('revendedores.id', ondelete='CASCADE')) # Para permitir deleção em cascade adiciono "ondelete='CASCADE'"
    revendedor: Mapped[Revendedor] = orm.relationship('Revendedor', lazy='joined', cascade='delete') # Para permitir deleção em cascade "cascade='delete'""
    
    # Relacionamento muitos-para-muitos com Lote
    lotes: Mapped[List[Lote]] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    
    def __repr__(self):
        return f'<Nota Fiscal: {self.numero_serie}>'
