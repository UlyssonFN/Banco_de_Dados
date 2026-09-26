#menu

def opcoes():
    print("Bem vindo ao Sistema de Vendas.")
    print("-----------------------------------")
    print("Escolha a opção abaixo do sistema:")
    print("1 - Cadastro de Usuários")
    print("2 - Realizar Venda")
    print("3 - Cadastrar Produtos")
    print("4 - Consultar Produtos")
    print("-----------------------------------")
    resp = int(input("Digite uma opção: "))
    
    match resp:
        case 1:
            print("1 - Tela: Cadastro de Usuários")
            from usuarios import user
        case 2:
            print("2 - Tela: Realizar Venda")
        case 3:
            print("3 - Tela: Cadastrar Produtos")
        case 4:
            print("4 - Tela: Consultar Produtos")

call = opcoes()
