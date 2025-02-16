import sqlite3
banco = sqlite3.connect('banco_car.sqlite')
cursor = banco.cursor()
cursor.execute('CREATE TABLE usuario(nome text , endereco text, cidade text, cpf text, habilitacao text, telefone text, email text )')
cursor.execute('CREATE TABLE cidade(nome text, uf text)')
cursor.execute('CREATE TABLE veiculos(marca text, modelo text, placa text, ano text, capacidade intger, proprietario text)')
banco.commit()


nome = input ('digite o nome:')
cpf = input ('digite o cpf:')
ende = input ('digite o endereço:')
cidade = input ('selecione a cidade:')
habilitacao = input ('digite a habilitação:')
telefone = input ('digite o telefone:')
email = input ('digite o email:')


cursor.execute (f"INSERT INTO usuario VALUES ('{nome}', '{ende}', '{cidade}', '{cpf}', '{habilitacao}', '{telefone}', '{email}' )")


uf = input ('digite a uf:')
nome = input ('digite o nome:')


cursor.execute (f"INSERT INTO usuario VALUES ('{nome}', '{uf}')")

ano = input ('digite o ano:')
placa = input ('digite a placa:')
modelo = input ('digite o modelo:')
marca = input ('digite a marca:')
capacidade = input ('digite a capacidade:')
proprietario = input ('digite proprietario:')


cursor.execute (f"INSERT INTO usuario VALUES ('{marca}', '{modelo}', '{placa}', '{ano}', '{capacidade}', '{proprietario}')")
banco.commit()