from questao_01 import q1
from questao_02 import q2
from questao_03 import q3

def menu():
    print('\nEscolha a baixo qual questão você deseja!\n'
          '|--------------|\n'
          '| Questão 1 - 1|\n'
          '| Questão 2 - 2|\n'
          '| Questão 3 - 3|\n'
          '|--------------|\n'
          '|Encerrar  -  0|')

print('Desafio Trainee Bemol - Etapa Python')
menu()

while True:
    opcao = input('Qual sua opção? ')
    print('')
    if opcao == '1':
        q1.media()
        print('\nProxima questão')
        menu()
    elif opcao == '2':
        q2.ranking()
        print('\nProxima questão')
        menu()
    elif opcao == '3':
        q3.valorProporcao()
        print('\nProxima questão')
        menu()
    elif opcao == '0':
        print('Fim das questões. Obrigado!')
        break
    else:
        print('Opção invalida')
        menu()