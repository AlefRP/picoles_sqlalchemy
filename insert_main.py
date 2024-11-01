from sqlalchemy.orm import Mapped, joinedload
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')
    
    nome: Mapped[str] = input('Informe o nome do aditivo nutritivo: ')
    formula_quimica: Mapped[str] = input('Informe a fórmula química do aditivo: ')
    
    an = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
    
    with create_session() as session:
        session.add(an)
        session.commit()
        
    return an


def insert_sabor() -> Sabor:
    print('Cadastrando Sabor')
    
    nome: Mapped[str] = input('Informe o nome do sabor: ')
    
    sabor = Sabor(nome=nome)
    
    with create_session() as session:
        session.add(sabor)
        session.commit()
        
    return sabor


def insert_tipo_embalagem() -> TipoEmbalagem:
    print('Cadastrando Tipo de Embalagem')
    
    nome: Mapped[str] = input('Informe o nome do Tipo de Embalagem: ')
    
    tipo_embalagem = TipoEmbalagem(nome=nome)
    
    with create_session() as session:
        
        session.add(tipo_embalagem)
        session.commit()
        
    return tipo_embalagem


def insert_tipo_picole() -> TipoPicole:
    print('Cadastrando Tipo de Picole')

    nome: Mapped[str] = input('Informe o nome do Tipo de Picole: ')

    tipo_picole = TipoPicole(nome=nome)

    with create_session() as session:

        session.add(tipo_picole)
        session.commit()

    return tipo_picole


def insert_ingrediente() -> Ingrediente:
    print('Cadastrando Ingrediente')

    nome: Mapped[str] = input('Informe o nome do Ingrediente: ')

    ingrediente = Ingrediente(nome=nome)

    with create_session() as session:

        session.add(ingrediente)
        session.commit()

    return ingrediente
    

def insert_conservante() -> Conservante:
    print('Cadastrando Conservante')
    
    nome: Mapped[str] = input('Informe o nome do Conservante: ')
    descricao: Mapped[str] = input('Informe a descrição do Conservante: ')
    
    conservante = Conservante(nome=nome, descricao=descricao)
    
    with create_session() as session:
        session.add(conservante)
        session.commit()
        
    return conservante


def insert_revendedor() -> Revendedor:
    print('Cadastrando Revendedor')
    
    cnpj: Mapped[str] = input('Informe o CNPJ do Revendedor: ')
    razao_social: Mapped[str] = input('Informe a razão social do Revendedor: ')
    contato: Mapped[str] = input('Informe o contato do Revendedor: ')
    
    revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
    
    with create_session() as session:
        session.add(revendedor)
        session.commit()
    
    return revendedor


def insert_lote() -> Lote:
    print('Cadastrando Lote')

    id_tipo_picole: Mapped[int] = int(input('Informe o ID do Tipo de Picole: '))
    quantidade: Mapped[int] = int(input('Informe a quantidade do Lote: '))
    
    lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    return lote


def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando Nota Fiscal')

    valor: Mapped[float] = float(input('Informe o valor da Nota Fiscal: '))
    numero_serie: Mapped[str] = input('Informe o número de série da Nota Fiscal: ')
    descricao: Mapped[str] = input('Informe a descrição da Nota Fiscal: ')

    # Criação do Revendedor usando a função existente
    revendedor = insert_revendedor()

    nf = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=revendedor.id)

    # Adiciona um lote usando a função existente
    lote = insert_lote()
    nf.lotes.append(lote)

    with create_session() as session:
        session.add(nf)
        session.commit()
        
        print(f'ID: {nf.id}')
        print(f'Data: {nf.data_criacao}')
        print(f'Valor: {nf.valor}')
        print(f'Numero de Serie: {nf.numero_serie}')
        print(f'Descrição: {nf.descricao}')
        print(f'ID Revendedor: {nf.id_revendedor}')
        print(f'Revendedor: {nf.revendedor.razao_social}')

    return nf


def insert_picole() -> Picole:
    print('Cadastrando Picole')

    preco: Mapped[float] = float(input('Informe o preço do Picole: '))
    id_sabor: Mapped[int] = int(input('Informe o ID do Sabor: '))
    id_tipo_picole: Mapped[int] = int(input('Informe o ID do Tipo de Picole: '))
    id_tipo_embalagem: Mapped[int] = int(input('Informe o ID do Tipo de Embalagem: '))

    picole = Picole(
        id_sabor=id_sabor,
        id_tipo_embalagem=id_tipo_embalagem,
        id_tipo_picole=id_tipo_picole,
        preco=preco
    )
    
    ingrediente_a = insert_ingrediente()
    picole.ingredientes.append(ingrediente_a)

    ingrediente_b = insert_ingrediente()
    picole.ingredientes.append(ingrediente_b)
    
    # Tem conservantes?
    conservante = insert_conservante()
    picole.conservantes.append(conservante)

    # Tem aditivos nutritivos?
    aditivo_nutritivo = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)
    
    with create_session() as session:
        session.add(picole)
        session.commit()

        print('Picole cadastrado com sucesso!')
        print(f'ID: {picole.id}')
        print(f'Data: {picole.data_criacao}')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Tipo de Picole: {picole.tipo_picole.nome}')
        print(f'Tipo de Embalagem: {picole.tipo_embalagem.nome}')
        print(f'Ingredientes: {picole.ingredientes}')
        print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
        print(f'Conservantes: {picole.conservantes}')

    return picole


if __name__ == '__main__':
    
    # 1 Aditivo Nutritivo
    # aditivo_nutritivo = insert_aditivo_nutritivo()
    # print('Aditivo Nutritivo cadastrado com sucesso!')
    # print(f'ID: {aditivo_nutritivo.id}')
    # print(f'Data: {aditivo_nutritivo.data_criacao}')
    # print(f'Nome: {aditivo_nutritivo.nome}')
    # print(f'Fórmula Química: {aditivo_nutritivo.formula_quimica}')
    
    # 2 Sabor
    # sabor = insert_sabor()
    # print('Sabor cadastrado com sucesso!')
    # print(f'ID: {sabor.id}')
    # print(f'Data: {sabor.data_criacao}')
    # print(f'Nome: {sabor.nome}')
    
    # 3 Tipo Embalagem
    # tipo_embalagem = insert_tipo_embalagem()
    # print('Tipo de Embalagem cadastrado com sucesso!')
    # print(f'ID: {tipo_embalagem.id}')
    # print(f'Data: {tipo_embalagem.data_criacao}')
    # print(f'Nome: {tipo_embalagem.nome}')
    
    # 4 Tipo Picole
    # tipo_picole = insert_tipo_picole()
    # print('Tipo de Picole cadastrado com sucesso!')
    # print(f'ID: {tipo_picole.id}')
    # print(f'Data: {tipo_picole.data_criacao}')
    # print(f'Nome: {tipo_picole.nome}')
    
    # 5 Ingrediente
    # ingrediente = insert_ingrediente()
    # print('Ingrediente cadastrado com sucesso!')
    # print(f'ID: {ingrediente.id}')
    # print(f'Data: {ingrediente.data_criacao}')
    # print(f'Nome: {ingrediente.nome}')
    
    # 6 Conservante
    # conservante = insert_conservante()
    # print('Conservante cadastrado com sucesso!')
    # print(f'ID: {conservante.id}')
    # print(f'Data: {conservante.data_criacao}')
    # print(f'Nome: {conservante.nome}')
    # print(f'Descrição: {conservante.descricao}')
    
    # 7 Revendedor
    # rev = insert_revendedor()
    # print(f'ID: {rev.id}')
    # print(f'Data: {rev.data_criacao}')
    # print(f'CNPJ: {rev.cnpj}')
    # print(f'Razão Social: {rev.razao_social}')
    
    # 8 Lote
    # lote = insert_lote()
    # print(f'ID: {lote.id}')
    # print(f'Data: {lote.data_criacao}')
    # print(f'ID Tipo Picole: {lote.id_tipo_picole}')
    # print(f'Quantidade: {lote.quantidade}')
    
    # 9 Nota Fiscal
    # insert_nota_fiscal()

    # 10 Picole
    insert_picole()