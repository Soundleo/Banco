import datetime

# Dicionário para armazenar os dados dos usuários
usuarios = {}

def cadastrar_usuario(nome):
    usuarios[nome] = {'saldo': 0.0, 'ultima_consulta': None}
    print(f"Usuário {nome} cadastrado com sucesso!")

def deletar_usuario(nome):
    if nome in usuarios:
        del usuarios[nome]
        print(f"Usuário {nome} deletado com sucesso!")
    else:
        print(f"Usuário {nome} não encontrado.")

def entrar(nome):
    if nome in usuarios:
        print(f"Bem-vindo de volta, {nome}!")
        return True
    else:
        print("Usuário não encontrado.")
        return False

def consultar_saldo(nome):
    if nome in usuarios:
        saldo = usuarios[nome]['saldo']
        ultima_consulta = usuarios[nome]['ultima_consulta']
        print(f"Saldo atual de {nome}: R$ {saldo:.2f}")
        if ultima_consulta:
            print(f"Última consulta realizada em: {ultima_consulta}")
        else:
            print("Nenhuma consulta anterior.")
        usuarios[nome]['ultima_consulta'] = datetime.datetime.now()
    else:
        print("Usuário não encontrado.")

def depositar(nome, valor):
    if nome in usuarios:
        usuarios[nome]['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso para {nome}.")
        consultar_saldo(nome)
    else:
        print("Usuário não encontrado.")

def sacar(nome, valor):
    if nome in usuarios:
        if usuarios[nome]['saldo'] >= valor:
            usuarios[nome]['saldo'] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso para {nome}.")
            consultar_saldo(nome)
        else:
            print(f"Saldo insuficiente para realizar o saque.")
            consultar_saldo(nome)
    else:
        print("Usuário não encontrado.")
