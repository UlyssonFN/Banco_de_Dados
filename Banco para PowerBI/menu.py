#menu

def opcoes():
    from funcoes import space
    print("Bem vindo ao Sistema de Vendas.")
    space()
    print("Escolha a opção abaixo do sistema:")
    print("1 - Cadastro de Usuários")
    print("2 - Realizar Venda")
    print("3 - Cadastrar Produtos")
    print("4 - Consultar Produtos")
    space()
    resp = int(input("Digite uma opção: "))
    
    match resp:
        case 1:
            print("1 - Tela: Cadastro de Usuários")
            space()
            from usuarios import user
            
            #depois tem que ajustar essa gambiarra, se bem que está funcional, por enquanto repetiremos o mesmo código para os outros cases.
        case 2:
            print("2 - Tela: Realizar Venda")
            space()
            
        case 3:
            print("3 - Tela: Cadastrar Produtos")
            space()
            from produtos import cad_produtos
            
        case 4:
            print("4 - Tela: Consultar Produtos")

call = opcoes()
