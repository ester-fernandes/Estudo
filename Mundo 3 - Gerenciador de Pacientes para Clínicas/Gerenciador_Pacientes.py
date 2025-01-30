import os

# Função para salvar os dados dos pacientes em um arquivo .txt
def salvar_dados(pacientes):
    with open('pacientes.txt', 'w') as file:
        for paciente in pacientes:
            file.write(f'Nome: {paciente["nome"]}\n')
            file.write(f'Idade: {paciente["idade"]}\n')
            file.write(f'Sintomas: {", ".join(paciente["sintomas"])}\n')
            file.write(f'Status da Consulta: {paciente["status_consulta"]}\n')
            file.write('-' * 20 + '\n')  # Separador entre os pacientes

# Função para carregar os dados dos pacientes do arquivo .txt
def carregar_dados():
    pacientes = []
    if os.path.exists('pacientes.txt'):
        with open('pacientes.txt', 'r') as file:
            dados_paciente = {}
            for line in file:
                line = line.strip()
                if line == '-' * 20:  # Separador entre os pacientes
                    pacientes.append(dados_paciente)
                    dados_paciente = {}
                elif line.startswith('Nome:'):
                    dados_paciente['nome'] = line.split(': ')[1]
                elif line.startswith('Idade:'):
                    dados_paciente['idade'] = int(line.split(': ')[1])
                elif line.startswith('Sintomas:'):
                    dados_paciente['sintomas'] = line.split(': ')[1].split(', ')
                elif line.startswith('Status da Consulta:'):
                    dados_paciente['status_consulta'] = line.split(': ')[1]
            # Adiciona o último paciente, se houver
            if dados_paciente:
                pacientes.append(dados_paciente)
    return pacientes


# Função para cadastrar um novo paciente
def cadastrar_paciente(pacientes):
    nome = input('Digite o nome do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    sintomas = input('Digite os sintomas [separados por vírgula]: ').split(',')
    status_consulta = 'pendente'  
    paciente = {
        'nome': nome,
        'idade': idade,
        'sintomas': sintomas,
        'status_consulta': status_consulta
    }
    pacientes.append(paciente)

# Função para listar todos os pacientes cadastrados
def listar_pacientes(pacientes):
    if not pacientes:
        print('Nenhum paciente cadastrado.')
    else:
        for paciente in pacientes:
            print(f'Nome: {paciente["nome"]}, Idade: {paciente["idade"]}, Sintomas: {", ".join(paciente["sintomas"])}, Status da Consulta: {paciente["status_consulta"]}')

# Função para atualizar as informações de um paciente
def atualizar_paciente(pacientes):
    nome = input('Digite o nome do paciente que deseja atualizar: ')
    for paciente in pacientes:
        if paciente['nome'].lower() == nome.lower():
            print('O que deseja atualizar?')
            print('1 - Nome')
            print('2 - Idade')
            print('3 - Sintomas')
            print('4 - Status da Consulta')
            escolha = input('Escolha uma opção: ')
            if escolha == '1':
                paciente['nome'] = input('Digite o novo nome: ')
            elif escolha == '2':
                paciente['idade'] = int(input('Digite a nova idade: '))
            elif escolha == '3':
                paciente['sintomas'] = input('Digite os novos sintomas (separados por vírgula): ').split(',')
            elif escolha == '4':
                paciente['status_consulta'] = input('Digite o novo status da consulta: ')
            else:
                print('Opção inválida!')
            break
    else:
        print('Paciente não encontrado.')

# Função para remover um paciente
def remover_paciente(pacientes):
    nome = input('Digite o nome do paciente que deseja remover: ')
    for paciente in pacientes:
        if paciente['nome'].lower() == nome.lower():
            pacientes.remove(paciente)
            print(f'Paciente {nome} removido com sucesso!')
            break
    else:
        print('Paciente não encontrado.')

# Função para consultar pacientes por sintomas
def consultar_por_sintoma(pacientes):
    sintoma_procurado = input('Digite o sintoma para consulta: ')
    pacientes_com_sintoma = [paciente for paciente in pacientes if sintoma_procurado.lower() in [s.lower() for s in paciente['sintomas']]]
    if pacientes_com_sintoma:
        for paciente in pacientes_com_sintoma:
            print(f'Nome: {paciente["nome"]}, Sintomas: {", ".join(paciente["sintomas"])}')
    else:
        print('Nenhum paciente com esse sintoma encontrado.')

# Função principal
def menu():
    pacientes = carregar_dados()
    while True:
        print('\n-- Menu de Gerenciamento de Pacientes --')
        print('1 - Cadastrar novo paciente')
        print('2 - Listar pacientes cadastrados')
        print('3 - Atualizar informações de um paciente')
        print('4 - Remover um paciente')
        print('5 - Consultar pacientes por sintoma')
        print('6 - Salvar e sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_paciente(pacientes)
        elif opcao == '2':
            listar_pacientes(pacientes)
        elif opcao == '3':
            atualizar_paciente(pacientes)
        elif opcao == '4':
            remover_paciente(pacientes)
        elif opcao == '5':
            consultar_por_sintoma(pacientes)
        elif opcao == '6':
            salvar_dados(pacientes)
            print('Dados salvos. Saindo...')
            break
        else:
            print('Opção inválida!')

# Executar o menu
menu()
