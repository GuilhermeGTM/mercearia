import controller
import os.path

def criarArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")


criarArquivos(
    "categoria.txt", "clientes.txt",
    "estoque.txt", "fornecedores.txt",
    "funcionarios.txt", "venda.txt")



if __name__ == "__main__":
    while True:
        local = int(input("----------------------------------------------\n"
                          "Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"
                          "----------------------------------------------\n"))

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    categoria = input("Digite a categoria que deseja cadastrar: ")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    print("----------------------------------------------")
                    categoria = input("Digite a categoria que deseja remover: ")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    print("----------------------------------------------")
                    categoria = input("Digite a categoria que deseja alterar: ")
                    novaCategoria = input("Digite a categoria para qual deseja alterar: ")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    print("----------------------------------------------")
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = controller.ControllerEstoque()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    nome = input("Digite o nome do produto: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = input("Digite a quantidade do produto: ")

                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    print("----------------------------------------------")
                    produto = input("Digite o produto que deseja remover: ")

                    cat.removerProduto(produto)
                elif decidir == 3:
                    print("----------------------------------------------")
                    nomeAlterar = input("Digite o nome do produto que deseja alterar: ")
                    nome = input("Digite o novo nome do produto: ")
                    preco = input("Digite o novo preco do produto: ")
                    categoria = input("Digite a nova categoria do produto: ")
                    quantidade = input("Digite a nova quantidade do produto: ")

                    cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    print("----------------------------------------------")
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            print("----------------------------------------------")
            cat = controller.ControllerFornecedor()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    nome = input("Digite o nome do fornecedor: ")
                    cnpj = input("Digite o cnpj do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    categoria = input("Digite a categoria fornecida: ")
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    print("----------------------------------------------")
                    fornecedor = input("Digite o fornecedor que deseja remover: ")
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    print("----------------------------------------------")
                    nomeAlterar = input("Digite o nome do fornecedor que deseja alterar: ")
                    novoNome = input('Digite o novo nome do fornecedor: ')
                    novoCnpj = input('Digite o novo cnpj do fornecedor: ')
                    novoTelefone = input('Digite o novo telefone do fornecedor: ')
                    novoCategoria = input('Digite a nova categoria fornecida: ')

                    cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria)
                elif decidir == 4:
                    print("----------------------------------------------")
                    cat.mostrarFornecedores()
                else:
                    break

        elif local == 4:
            cat = controller.ControllerCliente()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar clientes\n"
                                    "Digite 5 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    nome = input("Digite o nome do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    cpf = input("Digite o cpf do cliente: ")
                    email = input("Digite o email do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")

                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    print("----------------------------------------------")
                    cliente = input("Digite o cliente que deseja remover: ")

                    cat.removerCliente(cliente)
                elif decidir == 3:
                    print("----------------------------------------------")
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar: ")
                    novoNome = input("Digite o novo nome do cliente: ")
                    novoTelefone = input("Digite o novo telefone do cliente: ")
                    novoCpf = input("Digite o novo cpf do cliente: ")
                    novoEmail = input("Digite o novo email do cliente: ")
                    novoEndereco = input("Digite o novo endereço do cliente: ")
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    print("----------------------------------------------")
                    cat.mostrarClientes()
                else:
                    break

        elif local == 5:
            print("----------------------------------------------")
            cat = controller.ControllerFuncionario()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar funcionarios\n"
                                    "Digite 5 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    clt = input("Digite a clt do funcionario: ")
                    nome = input("Digite o nome do funcionario: ")
                    telefone = input("Digite o telefone do funcionario: ")
                    cpf = input("Digite o cpf do funcionario: ")
                    email = input("Digite o email do funcionario: ")
                    endereco = input("Digite o endereço do funcionario: ")

                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    print("----------------------------------------------")
                    funcionario = input("Digite o funcionario que deseja remover: ")
                    cat.removerFuncionario(funcionario)
                elif decidir == 3:
                    print("----------------------------------------------")
                    nomeAlterar = input("Digite o nome do funcionario que deseja alterar: ")
                    novoClt = input("Digite a nova clt do funcionario: ")
                    novoNome = input("Digite o novo nome do funcionario: ")
                    novoTelefone = input("Digite o novo telefone do funcionario: ")
                    novoCpf = input("Digite o novo cpf do funcionario: ")
                    novoEmail = input("Digite o novo email do funcionario: ")
                    novoEndereco = input("Digite o novo endereço do funcionario: ")
                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail,
                                           novoEndereco)

                elif decidir == 4:
                    print("----------------------------------------------")
                    cat.mostrarFuncionarios()
                else:
                    break

        elif local == 6:
            cat = controller.ControllerVenda()
            while True:
                decidir = int(input("----------------------------------------------\n"
                                    "Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"
                                    "----------------------------------------------\n"))

                if decidir == 1:
                    print("----------------------------------------------")
                    nome = input("Digite o nome do produto: ")
                    vendedor = input("Digite nome do vendedor: ")
                    comprador = input("Digite o nome do cliente: ")
                    quantidade = input("Digite a quantidade: ")
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    print("----------------------------------------------")
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano: ")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano: ")
                    cat.mostrarVenda(dataInicio, dataTermino)

        elif local == 7:
            a = controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break