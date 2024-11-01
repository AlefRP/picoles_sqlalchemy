# Projeto de Banco de Dados para Gerenciamento de Picoles com SQLAlchemy

Este projeto é uma aplicação Python utilizando SQLAlchemy para gerenciar registros relacionados a picoles, aditivos nutritivos, sabores, revendedores, dentre outros. Ele permite realizar operações CRUD (Create, Read, Update, Delete) e inclui consultas complexas para facilitar o gerenciamento de dados.

## Funcionalidades Principais

1. **Seleção de Dados**

   - Consultas simples e complexas para exibir registros.
   - Filtros por ID, ordenação por atributos e limite de resultados.
   - Agregações como soma, média, mínimo, máximo e contagem.

2. **Atualização de Registros**

   - Atualiza informações de sabores e picolés, com a possibilidade de alterar múltiplos atributos.

3. **Deleção de Registros**

   - Remove registros de forma segura, verificando a existência antes de proceder.

4. **Consultas Complexas**

   - Usa funções de grupo e ordenação para gerar estatísticas e relatórios.

## Estrutura do Projeto

- **conf**
  
  - `helpers.py`: Funções auxiliares, como a formatação de datas.
  - `db_session.py`: Configura a sessão de banco de dados.

- **models**
  - Contém os modelos de dados, como: `AditivoNutritivo`, `Sabor`, `Picole`, `Revendedor`, etc.

- **select_main.py**
  - Contém funções para consultas de dados, como seleção por ID e agregações.

- **update_main.py**
  - Define a lógica para atualizar registros, como sabores e preços de picolés.

- **delete_main.py**
  - Implementa a lógica para deletar registros de picolés e revendedores.

## Pré-requisitos

- **Python**: Versão 3.10 ou superior
- **Virtualenv**: Para gerenciamento de ambiente
- **Pacotes Python**: Listados no arquivo `requirements.txt`
  - `SQLAlchemy`

## Como Reproduzir o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-picoles.git
```

### 2. Instale as Dependências

```bash
cd projeto-picoles
pip install -r requirements.txt
```

### 3. Execute o Projeto

```bash
python select_main.py
```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE.md](LICENSE) para mais detalhes.
