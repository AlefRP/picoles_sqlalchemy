"""
1 - Buscar o registro a ser deletado;
2 - Fazer a deleção do objeto encontrado;
3 - Registrar no banco de dados a deleção;
"""

from typing import Optional
from conf.helpers import formata_data
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole


def delete_picole(id_picole: int) -> None:
    with create_session() as session:
        # Passo 1
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            # Passo 2
            session.delete(picole)
            # Passo 3
            session.commit()
        else:
            print(f'Nao encontrei picole com ID {id_picole}')

def delete_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        # Passo 1
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        
        if revendedor:
            # Passo 2
            session.delete(revendedor)
            # Passo 3
            session.commit()
            

def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Data: {formata_data(revendedor.data_criacao)}')
            print(f'Nome: {revendedor.razao_social}')
        else:
            print(f'Não existe revendedor com ID {id_revendedor}')



if __name__ == "__main__":
    from update_main import select_filtro_picole
    
    id_picole = 2
    
    # # Antes
    # select_filtro_picole(id_picole=id_picole)
    
    # # Deletar
    # delete_picole(id_picole=id_picole)
    
    # # Depois
    # select_filtro_picole(id_picole=id_picole)
    
    # id_revendedor = 43
    
    # Antes
    # select_filtro_revendedor(id_revendedor=id_revendedor)
    
    for id_revendedor in range(1, 31):
        delete_revendedor(id_revendedor=id_revendedor)
        
    # Deletar
    # delete_revendedor(id_revendedor=id_revendedor)
    
    # Depois
    # select_filtro_revendedor(id_revendedor=id_revendedor)
