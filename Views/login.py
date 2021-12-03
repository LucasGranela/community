
def main():
    print("")
    print("Escolha uma das opcoes a baixo:")
    print("")
    print("1 - Entrar como usuario comum")
    print("2 - Entrar como organizador")
    print("3 - Entrar como guarda")
    print("4 - Nao tenho conta")
    print("0 - Sair do programa")
    print("Entre com sua opcao:")
    opcao = input()

    return opcao

def login():
    print("")    
    email = input("Email: ")
    senha = input("Senha: ")

    return [email,senha]

def invalido():
    print("")
    print("Erro de login!")

def bemSucedido():
    print("")    
    print("Login bem-sucedido!")
