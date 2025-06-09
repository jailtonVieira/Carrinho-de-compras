#carrinho de compra

#lista do carrinho é a do usuario e a loja é o armazen 
carrinho = []

loja = {
    "01": {"nome": "abacate", "preco": 5.00},
    "02": {"nome": "abacaxi", "preco": 3.00},
    "03": {"nome": "acerola", "preco": 1.99},
    "04": {"nome": "banana", "preco": 8.00},
    "05": {"nome": "caja", "preco": 3.00},
    "06": {"nome": "goiaba", "preco": 1.99},
    "07": {"nome": "jaca", "preco" : 23.00},
    "08": {"nome": "kiwi", "preco" : 4.00},
    "09": {"nome": "laranja", "preco" : 1.50},
    "10": {"nome": "limao", "preco" : 1.00},
    "11": {"nome": "maca", "preco" : 2.00},
    "12": {"nome": "mamao", "preco" : 6.00},
    "13": {"nome": "manga", "preco" : 1.00},
    "14": {"nome": "maracuja", "preco" : 2.00},
    "15": {"nome": "melacia", "preco" : 22.00},
    "16": {"nome": "melao", "preco" : 7.00},
    "17": {"nome": "morango", "preco" : 1.20},
    "18": {"nome": "pera", "preco" : 5.00},
    "19": {"nome": "tanjerina", "preco" : 1.00},
    "20": {"nome": "uva", "preco" : 2.30},
}
# aqui é a entrada da loja

def inicio():
    print('Bem-vindo à loja do Fernando!')
    print('1 - Ir para o menu principal')
    print('2 - Mandar um feedback')
    saida1 = int(input('Qual opção? '))

    if saida1 == 1:
        main()
    elif saida1 == 2:
       erro()

    #aqui é omenu principal 

def main():
    print('Menu principal:')
    print('1 - Adicionar ao seu carrinho')
    print('2 - Remover do seu carrinho')
    print('3 - Sair do menu')
    print('4 - ver a sua lista')
    saida2 = int(input('Qual opção? '))

    if saida2 == 1:
        adicionar()
    elif saida2 == 2:
        deletar()
    elif saida2 == 3:
        inicio()
    elif saida2 == 4:
        verlist()
    else:
        print('Opção inválida.')
        main()

#aqui é uma funcao para adicionar a sua lista
#uso o for in range para pergunta quantos iten seram repetidos 

def adicionar():
    print('Este é o nosso catálogo:')
    for codigo, produto in loja.items():
        print(f"Código: {codigo}, Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    quantidade = int(input("Quantos itens você quer adicionar ao carrinho? "))

    for i in range(quantidade):
        codigo_produto = input(f"Digite o código do produto {i + 1}: ")
        if codigo_produto in loja:
            produto = loja[codigo_produto].copy()
            produto["id"] = codigo_produto 
            carrinho.append(produto)
            print(f"Produto {produto['nome']} adicionado ao carrinho!")
        else:
            print("Produto não encontrado.")

    print("Itens no carrinho:")
    for item in carrinho:
        print(f"{item['id']}: {item['nome']} - R${item['preco']:.2f}")

    print('1 - Deletar algum item')
    print('2 - Voltar para o menu')
    print('3 - Finalizar')
    saida3 = int(input('Qual a sua opção? '))

    if saida3 == 1:
        deletar()
    elif saida3 == 2:
        main()
    elif saida3 == 3:
        fianll()

#aqui ele confere qual codigo(id) que vc digitou e retira do carrinho
# o if not ele confere se a verificação não é verddadeira

def deletar():
    if not carrinho:
        print("Seu carrinho está vazio!")
        return

    print("Itens no carrinho:")
    for item in carrinho:
        print(f"{item['id']}: {item['nome']} - R${item['preco']:.2f}")

    id_item = input("Digite o código do item que deseja remover: ")
    encontrado = False

    for i, item in enumerate(carrinho):
        if item["id"] == id_item:
            del carrinho[i]
            encontrado = True
            print("Item removido")
            break

    if not encontrado:
        print("Item não encontrado no carrinho.")

    print("Carrinho atualizado:")
    for item in carrinho:
        print(f"{item['id']}: {item['nome']} - R${item['preco']:.2f}")

    main()

def erro():
    print('caso de achou algum erro mande um feeddback para nos:')
    feedback = str(input('qual o seu feedback:'))
    print('seu feedback foi recebedido com sucesso')

def fianll():
    print('obrido por realizar uma compra no nosso site')

def verlist():
    print(carrinho)

inicio()
