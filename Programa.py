# função para validar se a entrada do usuário é um número inteiro
def validar_int(texto):
    while True:
        try:
            valor = int(input(texto))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

# função para validar se a entrada do usuário é um número real
def validar_float(texto):
    while True:
        try:
            valor = float(input(texto))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número real.")

# loop principal que permite cadastrar vários pedidos
while True:
    # solicita o nome do cliente
    nome = input("Digite o nome do cliente: ")

    # solicita a quantidade de produtos
    qtde_produtos = validar_int("Digite a quantidade de produtos: ")

    # cria um dicionário para armazenar o valor total de cada pedido
    total_pedidos = {}

    # lista para armazenar os detalhes de cada produto
    detalhes_produtos = []

    # solicita os detalhes de cada produto e armazena na lista
    for i in range(qtde_produtos):
        print(f"\nProduto {i + 1}:")
        nome_produto = input("Digite o nome do produto: ")
        qtde_produto = validar_int("Digite a quantidade do produto: ")
        preco_produto = validar_float("Digite o preço unitário do produto: ")
        detalhes_produtos.append([nome_produto, qtde_produto, preco_produto])

    # calcula o valor total do pedido
    valor_total = 0
    for detalhes in detalhes_produtos:
        valor_total += detalhes[1] * detalhes[2]

    # adiciona o valor total do pedido ao dicionário
    total_pedidos[nome] = valor_total

    # exibe o valor total do pedido na tela
    print(f"\nValor total do pedido: R$ {valor_total:.2f}\n")

    # pergunta ao usuário se deseja cadastrar um novo pedido
    opcao = input("Deseja cadastrar um novo pedido? (S/N) ")

    # se o usuário não quiser cadastrar um novo pedido, sai do loop principal
    if opcao.upper() != "S":
        break

# cria o arquivo pedidos.txt e grava as informações de cada pedido
with open("pedidos.txt", "w") as arquivo_pedidos:
    for nome, valor_total in total_pedidos.items():
        # escreve o nome do cliente no arquivo
        arquivo_pedidos.write(nome + "\n")

        # escreve os detalhes de cada produto no arquivo
        for detalhes in detalhes_produtos:
            arquivo_pedidos.write(",".join(str(d) for d in detalhes) + "\n")

# cria o arquivo total_pedidos.txt e grava o valor total de cada pedido
with open("total_pedidos.txt", "w") as arquivo_total_pedidos:
    for nome, valor_total in total_pedidos.items():
        arquivo_total_pedidos.write(nome + " - R$ " + str(valor_total) + "\n")

print("Programa finalizado.")
