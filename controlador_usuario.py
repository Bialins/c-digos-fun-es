def autenticar(login, senha):
    usuarios = [
        {'login': 'usuario123', 'senha': 'senha123'},
        {'login': 'usuario456', 'senha': 'senha456'},
        {'login': 'usuario789', 'senha': 'senha789'},
    ]

    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            return True  
    
    return False  


if __name__ == "__main__":
    login_input = input('Digite seu login: ')
    senha_input = input('Digite sua senha: ')

    if autenticar(login_input, senha_input):
        print('Autenticação bem-sucedida.')
    else:
        print('Login ou senha incorretos.')

    