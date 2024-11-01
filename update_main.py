"""
1 - Buscar o registro a ser atualizado;
2 - Efetuar as alterações no registro;
3 - Salvar as alterações no banco de dados.
"""

from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole
from select_main import select_filtro_sabor


def select_filtro_picole(id_picole: int) -> Picole | None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            print(f'ID: {picole.id}')
            print(f'Data: {picole.data_criacao}')
            print(f'Sabor: {picole.sabor.nome}')
        else:
            print(f'Não existe picole com ID {id_picole}')


def update_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        if sabor:
            sabor.nome = novo_nome
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')

          
def update_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também...
            if novo_sabor:
                picole.id_sabor = novo_sabor
            session.commit()
        else:
            print(f'Não existe picole com ID {id_picole}')


if __name__ == '__main__':
    
    id_sabor = 3
    
    # Antes
    select_filtro_sabor(id_sabor=id_sabor)
    
    # Atualizando
    # update_sabor(id_sabor=id_sabor, novo_nome='Mangarin')
    
    # Depois
    # select_filtro_sabor(id_sabor=id_sabor)
    
    id_picole = 2
    
    # Antes de atualizar o picole
    select_filtro_picole(id_picole=id_picole)
    
    # Atualizando o picole
    update_picole(id_picole=id_picole, novo_preco=9.99, novo_sabor=2)
    
    # Depois de atualizar o picole
    select_filtro_picole(id_picole=id_picole)