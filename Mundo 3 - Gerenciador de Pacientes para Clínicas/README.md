# Gerenciador de Pacientes para Clínicas

## Descrição

Este é um sistema simples de gerenciamento de pacientes para clínicas. O programa permite cadastrar novos pacientes, listar os pacientes cadastrados, atualizar suas informações, remover pacientes e consultar pacientes com base em sintomas específicos. Além disso, os dados dos pacientes são salvos e carregados de um arquivo de texto.

## Tecnologias Utilizadas

- Python (versão 3.x recomendada)
- Módulos: os (para verificação de arquivos)
- Arquivo de Dados: .txt (para salvar e carregar os dados dos pacientes)

## Funcionalidades

- **Cadastrar Paciente**: O usuário pode cadastrar um paciente, informando nome, idade, sintomas e status da consulta.
- **Listar Pacientes**: Exibe todos os pacientes cadastrados com seus detalhes.
- **Atualizar Paciente**: Permite atualizar os dados de um paciente (nome, idade, sintomas ou status da consulta).
- **Remover Paciente**: Exclui um paciente do sistema.
- **Consultar Pacientes por Sintomas**: Permite procurar pacientes com base em sintomas informados.
- **Salvar Dados**: Os dados dos pacientes são salvos em um arquivo .txt ao final, para serem carregados na próxima execução.

## Como Rodar o Projeto

1. Faça o download do arquivo do código Python (gerenciador_pacientes.py).
2. Certifique-se de que você tem o Python 3.x instalado.
3.  Execute o script no terminal ou IDE de sua preferência.

bash
python gerenciador_pacientes.py

## Como Rodar os Testes

Este projeto não possui testes automatizados, mas você pode testar o funcionamento manualmente executando o código e interagindo com as opções no menu.

## Problemas Encontrados

Nenhum problema foi encontrado durante o desenvolvimento do projeto.

## Próximos Passos

- Adicionar validação de inputs para garantir dados corretos (exemplo: validar a idade como um número positivo).
- Melhorar o tratamento de exceções (exemplo: ao carregar ou salvar o arquivo de dados).
- Implementar funcionalidades adicionais como o agendamento de consultas.
- Criar uma interface gráfica para melhorar a experiência do usuário.