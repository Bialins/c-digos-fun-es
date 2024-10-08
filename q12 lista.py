def verificar_email(email):
    return '@' in email

if __name__ == "__main__":
    email_input = input("Digite um email: ")
    resultado = verificar_email(email_input)

    if resultado:
        print("O email contém '@'.")
    else:
        print("O email não contém '@'.")
