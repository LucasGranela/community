
def main():
    print("")
    print("Escolha uma das opcoes a baixo:")
    print("")
    print("1 - Ocorrências")
    print("2 - Eventos")
    print("3 - Pontos estrategicos")
    print("4 - Posts geral")
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
