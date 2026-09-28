#menu

def opcoes_f():
    from funcoes import space
    from usuarios import user_f
    from produtos import cad_produtos_f
    from vendas import vendas_f
    
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
            user_f()
            
            #depois tem que ajustar essa gambiarra, se bem que está funcional, por enquanto repetiremos o mesmo código para os outros cases.
        case 2:
            print("2 - Tela: Realizar Venda")
            space()
            vendas_f()
            
        case 3:
            print("3 - Tela: Cadastrar Produtos")
            space()
            cad_produtos_f()
            
        case 4:
            print("4 - Tela: Consultar Produtos")
