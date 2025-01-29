'''
Crie um programa que simule uma loja virtual. O usuário pode adicionar itens ao carrinho, visualizar o total, remover itens e finalizar a compra.
'''

print('-'*15)
print('Loja Virtual')
print('-'*15)

import random
from time import sleep

itens_disponiveis = [ 'Camiseta', 'Calça', 'Tênis', 'Jaqueta', 'Bermuda',]

def gerar_preco():
    return round(random.uniform(20.0, 200.0), 2)

carrinho = []
def adicionar_ao_carrinho():
    print('\nEscolha um item:')
    for i, item in enumerate(itens_disponiveis, start=1):
        print(f'{i}. {item}')

    escolha_item = int(input('\nDigite o número do item: ')) - 1
    quantidade = int(input('Quantos deseja adicionar? '))
    
    item_escolhido = itens_disponiveis[escolha_item]
    preco_item = gerar_preco()
    carrinho.append({'item': item_escolhido, 'quantidade': quantidade, 'preco': preco_item})
    print(f'{quantidade} {item_escolhido}(s) adicionados ao carrinho.')

def visualizar_carrinho():
    if not carrinho:
        print('\nCarrinho vazio.')
        return
    print("\nCarrinho de Compras:")
    for item in carrinho:
        print(f"{item['quantidade']}x {item['item']} - R$ {item['preco']:.2f} cada")

def remover_item():
    visualizar_carrinho()
    if carrinho:
        item_remover = int(input("\nDigite o número do item que deseja remover: ")) - 1
        del carrinho[item_remover]
        print('Item removido com sucesso.')

def calcular_total():
    total = sum(item['preco'] * item['quantidade'] for item in carrinho)
    print(f'\nTotal: R$ {total:.2f}')

def obter_numero_carrinho(nome):
    try:
        with open('dados_cliente.txt', 'r') as file:
            conteudo = file.readlines()
            contador = 0
            for linha in conteudo:
                if f'Cliente: {nome}' in linha:
                    contador += 1
            return contador + 1  
    except FileNotFoundError:
        return 1

def salvar_dados(nome, carrinho):
    numero_carrinho = obter_numero_carrinho(nome)

    with open('dados_cliente.txt', 'a') as file:
        file.write(f'\nCliente: {nome}\n')
        file.write(f'\nCarrinho {numero_carrinho}:\n')
        for item in carrinho:
            file.write(f"{item['quantidade']}x {item['item']} - R$ {item['preco']:.2f} cada\n")
        total = sum(item['preco'] * item['quantidade'] for item in carrinho)
        file.write(f'Total: R$ {total:.2f}\n')
    print('Dados salvos com sucesso!')

def finalizar_compras():
    print('Finalizando compras...')
    sleep(3)
    salvar_dados(nome, carrinho)
    print('Compra finalizada. Obrigado por comprar!')


nome = str(input('Digite o seu nome: '))

while True:
    print('\nMENU:')
    print('''
[1] Adicionar Itens ao Carrinho
[2] Visualizar Carrinho
[3] Remover Itens
[4] Total          
[5] Finalizar Compras''')
    
    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 1:
        adicionar_ao_carrinho()

    elif opcao == 2:
        visualizar_carrinho()

    elif opcao == 3:
        remover_item()

    elif opcao == 4:
        calcular_total()

    elif opcao == 5:
        finalizar_compras()
        break

    else:
        print('Opção inválida, tente novamente')