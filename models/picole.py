import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo
from sqlalchemy.orm import Mapped, mapped_column
from typing import List, Optional

# Tabelas de associação para os relacionamentos muitos-para-muitos
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
)

conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservante', sa.Integer, sa.ForeignKey('conservantes.id'))
)

aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id'))
)

class Picole(ModelBase):
    __tablename__ = 'picoles'
    
    preco: Mapped[float] = mapped_column(sa.DECIMAL(8, 2), nullable=False)
    
    id_sabor: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Mapped[Sabor] = orm.relationship('Sabor', lazy='joined')
    
    id_tipo_embalagem: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: Mapped[TipoEmbalagem] = orm.relationship('TipoEmbalagem', lazy='joined')
    
    id_tipo_picole: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined')
    
    # Relacionamento muitos-para-muitos com Ingrediente
    ingredientes: Mapped[List[Ingrediente]] = orm.relationship(
        'Ingrediente', 
        secondary=ingredientes_picole, 
        backref='ingrediente', 
        lazy='joined'
    )
    
    # Relacionamento muitos-para-muitos com Conservante (opcional)
    conservantes: Mapped[Optional[List[Conservante]]] = orm.relationship(
        'Conservante', 
        secondary=conservantes_picole, 
        backref='conservante', 
        lazy='joined'
    )
    
    # Relacionamento muitos-para-muitos com Aditivo Nutritivo (opcional)
    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship(
        'AditivoNutritivo', 
        secondary=aditivos_nutritivos_picole, 
        backref='aditivo_nutritivo', 
        lazy='joined'
    )
    
    def __repr__(self):
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preco {self.preco}>'
