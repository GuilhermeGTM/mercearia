from models import Categoria, Produtos, Estoque, Fornecedor, Pessoa, Funcionario, Venda
from dao import DaoCategoria, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario, DaoVenda
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada.')
        else:
            print('Categoria cadastrada já existe.')
    
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        # retorna a categoria = a categoria que foi digitada
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        # se a lista cat retornar 0, caso contrario retornaria o numero de caracteres do que foi 
        # digitado pq o lambda acima retorna o numero na lista cat
        if len(cat) <= 0:
            print('Categoria que deseja remover não existe.')
        else: # se a categoria digitada existir
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i] # deleta
                    break
            print('Categoria removida.')
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem categoria"),
                                             x.quantidade) if(x.produto.categoria == categoriaRemover)
                                             else(x),estoque))
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria
                               + "|" + str(i.quantidade))
                arq.writelines("\n")

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        
        
        cat =  list(filter(lambda x: x.categoria == categoriaAlterar, x))

        # verifica se a categoria que deseja alterar existe  ou não existe
        # se existe
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                # substitue a categoria por outra
                x = list(map(lambda x: Categoria(categoriaAlterada) 
                             if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada.')
                
                estoque = DaoEstoque.ler()

                estoque = list(map(
                    lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) if (
                                x.produto.categoria == categoriaAlterar) else (x), estoque))
                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                            i.quantidade))
                        arq.writelines("\n")

            else:
              print('Categoria para qual deseja alterar já existe.')
        # se não existe
        else:
            print('Categoria que deseja alterar não existe.')
        
        # rerescreve no arquivo
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else: 
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto já existe em estoque.')
        else:
            print('Categoria inexistente.')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est =  list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto Removido.')
        else:
            print('Produto não existe')
        
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                           i.produto.categoria + "|" + str(i.quantidade))
            arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado.')
                else:
                    print('Produto já cadastrado.')
            else:
                print('Produto não existe.')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                                   i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('Categoria não existe.')

    def mostrarEstoque(self):
        estoque =  DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print("========Produtos========")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}"
                      )
                print('-------------------------')


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write("")


        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

        if existe == False:
            print('Produto não existe.')
            return None
        elif not quantidade:
            print('Quantidade vendida não contem em estoque.')
            return None
        else:
            print('Venda realizada.')
            return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Produtos mais vendidos.')
        a = 1
        for i in ordenado:
            print(f"==========Produto [{a}] ==========")
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendido.nome}\n"
                  f"Categoria: {i.itensVendido.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}"
                  )
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1

        print(f"Total vendido: {total}")


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print("Cnpj já existe.")
        elif len(listaTelefone) > 0:
            print('Telefone já existe.')
        else:
            if len(cnpj)  == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado.')
            else:
                print("Digite um cnpj ou telefone válido")

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria)
                             if(x.nome == nomeAlterar) else(x),x))
                print('Fornecedor alterado.')
            else:
                print('Cnpj já existe.')
        else:
            print('Fornecedor que deseja alterar nao existe.')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('Fornecedor que deseja remover não existe.')
            return None

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido.')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("Lista de fornecedores vazia.")

        for i in fornecedores:
            print("=========Fornecedores==========")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Cnpj: {i.cnpj}")


class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente Cadastrado.')
            else:
                print('Digite um cpf ou telefone válido.')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                         if (x.nome == nomeAlterar) else (x), x))
            print('Cliente alterado.')
        else:
            print('Cliente que deseja alterar nao existe.')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('Cliente que deseja remover não existe.')
            return None

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Cliente removido.')

    def mostrarClientes(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Lista de clientes vazia.")

        for i in clientes:
            print("=========Cliente=========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"CPF: {i.cpf}")


class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('CPF já existe.')
        elif len(listaClt) > 0:
            print('Já existe um funcionario com essa clt.')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado.')
            else:
                print('Digite um cpf ou telefone válido.')

    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt,novoNome, novoTelefone, novoCpf,
                                               novoEmail, novoEndereco) if (x.nome == nomeAlterar) else (x), x))
            print('Funcionario alterado.')
        else:
            print('Funcionario que deseja alterar nao existe.')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email
                               + "|" + i.endereco)
                arq.writelines('\n')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('Funcionario que deseja remover não existe.')
            return None

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionarios removido.')

    def mostrarFuncionarios(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print("Lista de funcionarios vazia.")

        for i in funcionario:
            print("========Funcionario==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}\n")


