from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sqlite3
cidades = []

veiculos = []

usuarios = []
banco = sqlite3.connect('banco_car.sqlite')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS usuario(nome text , endereco text, cidade text, cpf text, habilitacao text, telefone text, email text )')
cursor.execute('CREATE TABLE IF NOT EXISTS cidade(nome text, uf text)')
cursor.execute('CREATE TABLE IF NOT EXISTS veiculos(marca text, modelo text, placa text, ano text, capacidade integer, proprietario text)')
banco.commit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def submit_cidade(txtnome, txtuf):
    cidade_info = f'{txtnome.get()}, {txtuf.get().upper()}'
    cidades.append(cidade_info)
    cursor.execute(f"INSERT INTO cidade VALUES ('{txtnome.get()}', '{txtuf.get()}')")
    banco.commit()
def cidade():
    cidade = Toplevel()
    cidade.geometry("300x200")
    cidade.title("cidade")

    lbluf = Label(cidade, text="uf:")
    lblnome = Label(cidade, text="nome:")

    lbluf.grid(row=1, column=0, padx=5, pady=5)
    lblnome.grid(row=2, column=0, padx=5, pady=5)

    txtuf = Entry(cidade)
    txtnome = Entry(cidade)

    txtuf.grid(row=1, column=1, padx=5, pady=5)
    txtnome.grid(row=2, column=1, padx=5, pady=5)

    btnSubmit = Button(cidade, text="submit", command=lambda: submit_cidade(txtnome, txtuf))
    btnSubmit.grid(row=6, column=0, padx=5, pady=5)

    cidade.focus_set()
    cidade.grab_set()
    cidade.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def submit_usuario():
    nome = usuarios[0].get()
    cpf = usuarios[1].get()
    ende = usuarios[2].get()
    cidade = usuarios[3].get()
    habilitacao = usuarios[4].get()
    cel = usuarios[5].get()
    email = usuarios[6].get()

    cursor.execute(f"INSERT INTO usuario VALUES ('{nome}', '{ende}', '{cidade}', '{cpf}', '{habilitacao}', '{cel}', '{email}' )")
    banco.commit()

def carregar_cidades():
    cursor.execute("SELECT nome FROM cidade")
    cidades.clear()  # Limpa a lista antes de atualizar
    for row in cursor.fetchall():
        cidades.append(row[0])

def usuario():
    carregar_cidades()  # Atualiza a lista antes de abrir a janela

    usuario = Toplevel()
    usuario.geometry("700x400")
    usuario.title("Usuário")

    lblnome = Label(usuario, text="Nome:")
    lblcpf = Label(usuario, text="CPF:")
    lblende = Label(usuario, text="Endereço:")
    lblcidade = Label(usuario, text="Cidade:")
    lblhabilitacao = Label(usuario, text="Habilitação:")
    lblcel = Label(usuario, text="Cel:")
    lblemail = Label(usuario, text="Email:")

    lblnome.grid(row=0, column=0, padx=5, pady=5)
    lblcpf.grid(row=1, column=0, padx=5, pady=5)
    lblende.grid(row=2, column=0, padx=5, pady=5)
    lblcidade.grid(row=3, column=0, padx=5, pady=5)
    lblhabilitacao.grid(row=4, column=0, padx=5, pady=5)
    lblcel.grid(row=5, column=0, padx=5, pady=5)
    lblemail.grid(row=6, column=0, padx=5, pady=5)

    txtnome = Entry(usuario)
    txtcpf = Entry(usuario)
    txtende = Entry(usuario)
    txthabilitacao = Entry(usuario)
    txtcel = Entry(usuario)
    txtemail = Entry(usuario)

    txtnome.grid(row=0, column=1, padx=5, pady=5)
    txtcpf.grid(row=1, column=1, padx=5, pady=5)
    txtende.grid(row=2, column=1, padx=5, pady=5)
    txthabilitacao.grid(row=4, column=1, padx=5, pady=5)
    txtcel.grid(row=5, column=1, padx=5, pady=5)
    txtemail.grid(row=6, column=1, padx=5, pady=5)

    n = tk.StringVar()
    monthchoosen = Combobox(usuario, width=17, textvariable=n, values=cidades)
    monthchoosen.grid(column=1, row=3)

    usuarios.clear()
    usuarios.append(txtnome)
    usuarios.append(txtcpf)
    usuarios.append(txtende)
    usuarios.append(monthchoosen)  # Aqui está a correção para cidade
    usuarios.append(txthabilitacao)
    usuarios.append(txtcel)
    usuarios.append(txtemail)

    btnSubmit = Button(usuario, text="Submit", command=submit_usuario)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    usuario.focus_set()
    usuario.grab_set()
    usuario.mainloop()
   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_veiculo():
    ano = veiculos[0].get()
    placa = veiculos[1].get()
    modelo = veiculos[2].get()
    marca = veiculos[3].get()
    capacidade = veiculos[4].get()
    proprietario = veiculos[5].get()
    cursor.execute(f"INSERT INTO veiculos VALUES ('{ano}', '{placa}', '{modelo}', '{marca}', {capacidade}, '{proprietario}')")
    banco.commit()

def veiculo():
    veiculo = Toplevel()
    veiculo.geometry("300x300")
    veiculo.title("veiculo")

    lblano = Label(veiculo, text="ano:")
    lblplaca = Label(veiculo, text="placa:")
    lblmodelo = Label(veiculo, text="modelo:")
    lblmarca = Label(veiculo, text="marca:")
    lblcapacidade = Label(veiculo, text="capacidade:")
    lblproprietario = Label(veiculo, text="proprietario:")

    lblano.grid(row=0, column=0, padx=5, pady=5)
    lblplaca.grid(row=1, column=0, padx=5, pady=5)
    lblmodelo.grid(row=2, column=0, padx=5, pady=5)
    lblmarca.grid(row=3, column=0, padx=5, pady=5)
    lblcapacidade.grid(row=4, column=0, padx=5, pady=5)
    lblproprietario.grid(row=5, column=0, padx=5, pady=5)

    txtano = Entry(veiculo)
    txtplaca = Entry(veiculo)
    txtmodelo = Entry(veiculo)
    txtmarca = Entry(veiculo)
    txtcapacidade = Entry(veiculo)
    txtproprietario = Entry(veiculo)

    txtano.grid(row=0, column=1, padx=5, pady=5)
    txtplaca.grid(row=1, column=1, padx=5, pady=5)
    txtmodelo.grid(row=2, column=1, padx=5, pady=5)
    txtmarca.grid(row=3, column=1, padx=5, pady=5)
    txtcapacidade.grid(row=4, column=1, padx=5, pady=5)
    txtproprietario.grid(row=5, column=1, padx=5, pady=5)

    
    veiculos.append(txtano)
    veiculos.append(txtplaca)
    veiculos.append(txtmodelo)
    veiculos.append(txtmarca)
    veiculos.append(txtcapacidade)
    veiculos.append(txtproprietario)


    btnSubmit = Button(veiculo, text="submit", command=submit_veiculo)
    btnSubmit.grid(row=7, column=0, padx=5, pady=5)

    veiculo.focus_set()
    veiculo.grab_set()
    veiculo.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    janela_principal = Tk()
    janela_principal.geometry("350x250")
    janela_principal.title("janela")


    btn2 = Button(janela_principal, text="cidade", command=cidade)
    btn1 = Button(janela_principal, text="veiculo", command=veiculo)
    btn = Button(janela_principal, text="usuario", command=usuario)

    btn.grid(row=0, column=2, padx=10, pady=10)
    btn1.grid(row=0, column=1, padx=10, pady=10)
    btn2.grid(row=0, column=0, padx=10, pady=10)

    janela_principal.mainloop()

if __name__ == "__main__":
    main()
