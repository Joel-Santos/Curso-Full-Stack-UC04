from controllers.produto_controller import ProdutoController

def menu():
    print("\n--- CRUD de Produtos ---")
    print("1. Criar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("0. Sair")
    return input("Escolha uma opção:")

if __name__ == "__main__":
    controller = ProdutoController()

while True:
    opcao = menu()
    if opcao == "1":
        id = int(input("Digite o ID do Produto:"))
        nome = input("Digite o Nome do Produto:")
        preco = float(input("Digite o Preço do Produto:"))
        controller.criar_produto(id, nome, preco)
    elif opcao == "2":
        controller.listar_produtos()
    elif opcao == "0":
        print("Encerrando")
        break
    else:
        print("Opção Invalida")