'''
1. Solicitar os dados: nome, idade, peso(em kg) e altura(em metros)

2.Calcular o IMC: IMC = peso / (altura**2)

3.Classificar o IMCe retornar a classificação correta: 
- Abaixo = <18.5
- Normal =  18.5 <= < 25
- Sobrepeso = 25 <= <30
Obesidade 1 = 30 <= <35
Obesidade 2 = 35 <= <40
Obesidade 3 = >= 40

4.Mensagem personalizada

5. Estrutura de Repetição:
- Perguntar se quer calcular o IMC de outra pessoa

6. Calcular a média de IMC de todas as pessoas cadastradas ao final do programa

7. Salvar os dados de cada pessoa(nome, idade, IMC e classificação) em uma lista e exibi-los no final
'''

print('-=-'*20)
print('Bem-vindo a Calculadora de IMC!\nVamos começar?')
print('-=-'*20)

# 1. Solicitar os dados: nome, idade, peso(em kg) e altura(em metros)
nome = str(input('Digite o seu nome: ')).strip()
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso em kg:'))
altura = float(input('Digite a sua altura em metros:'))

# 2.Calcular o IMC: IMC = peso / (altura**2)
imc = peso / altura**2

# 3/4.Classificar o IMCe retornar a classificação correta e Mensagem personalizada:
clas1 = 'Abaixo do Peso'
clas2 = 'Peso Normal'
clas3 = 'Sobrepeso'
clas4 = 'Obesidade tipo I'
clas5 = 'Obesidade tipo II'
clas6 = 'Obesidade tipo III'

if imc < 18.5:
    classificacao = clas1
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem.\nMas, outras podem estar enfrentando problemas, como a desnutrição.\nProcure um médico ou um nutricionista para saber se está tudo bem com você.')
elif 18.5 <= imc < 25:
    classificacao = clas2
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('Parabéns, que bom que você está com o peso normal!\nMantenha um estilo de vida saudável com uma alimentação equilibrada e atividades físicas.')
elif 25 <= imc < 30:
    classificacao = clas3
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('CUIDADO!!\nÉ importante rever os seu hábitos e buscar ajuda antes de que, por vários fatores, você possa entrar na faixa da obesidade.\nFique de olho!')
elif 30 <= imc < 35:
    classificacao = clas4
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('\033[33mATENÇÃO!!!\033[0m\nVamos dar início as mudanças hoje!!\nProcure um médico ou um nutricionista para te ajudar.\nVamos lá, você consegue!')
elif 35 <= imc < 40:
    classificacao = clas5
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('Tá na hora de se cuidar!\nVamos iniciar mudanças no estilo de vida com acompanhamento de profissionais da saúde.\nVamos cuidar da sua saúde!')
else:
    classificacao = clas6
    print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
    print('\033[31mALERTA VERMELHO!!!\033[0m\nProcure ajuda médica imediatamente.')

# 5. Estrutura de Repetição e salvar os dados de cada pessoa:
dados_pessoas = []

while True:
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        print('Obrigado por usar a Calculadora de IMC!')
        break
    else:
        print('Ótimo!!\nVamos continuar.')

#Entrada de dados
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    peso = float(input('Digite o seu peso em kg: '))
    altura = float(input('Digite a sua altura em metros:'))
    imc = peso / altura**2

    if imc < 18.5:
        classificacao = clas1
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem.\nMas, outras podem estar enfrentando problemas, como a desnutrição.\nProcure um médico ou um nutricionista para saber se está tudo bem com você.')
    elif 18.5 <= imc < 25:
        classificacao = clas2
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('Parabéns, que bom que você está com o peso normal!\nMantenha um estilo de vida saudável com uma alimentação equilibrada e atividades físicas.')
    elif 25 <= imc < 30:
        classificacao = clas3
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('CUIDADO!!\nÉ importante rever os seu hábitos e buscar ajuda antes de que, por vários fatores, você possa entrar na faixa da obesidade.\nFique de olho!')
    elif 30 <= imc < 35:
        classificacao = clas4
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('\033[33mATENÇÃO!!!\033[0m\nVamos dar início as mudanças hoje!!\nProcure um médico ou um nutricionista para te ajudar.\nVamos lá, você consegue!')
    elif 35 <= imc < 40:
        classificacao = clas5
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('Tá na hora de se cuidar!\nVamos iniciar mudanças no estilo de vida com acompanhamento de profissionais da saúde.\nVamos cuidar da sua saúde!')
    else:
        classificacao = clas6
        print(f'Olá {nome}!\nO seu IMC é de {imc:.2f} e a sua classificação é {classificacao}.')
        print('\033[31mALERTA VERMELHO!!!\033[0m\nProcure ajuda médica imediatamente.')

#Salvar os dados de cada pessoa em um dicionário:
    dados_pessoas.append({
        'nome': nome,
        'idade': idade,
        'imc': imc,
        'classificacao': classificacao
    })
# 6. Calcular a média de IMC de todas as pessoas cadastradas ao final do programa
if len(dados_pessoas) > 0: #Verificar se há dados cadastrados e quantas pessoas foram cadastradas
    soma_imc = sum(pessoa["imc"] for pessoa in dados_pessoas)
    media_imc = soma_imc / len(dados_pessoas)

    print("\n-=- Resumo dos dados cadastrados -=-")
    for pessoa in dados_pessoas:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, IMC: {pessoa['imc']:.2f}, Classificação: {pessoa['classificacao']}")
    print(f"\nMédia de IMC de todas as pessoas cadastradas: {media_imc:.2f}")
else:
    print("Nenhum dado foi cadastrado.")

