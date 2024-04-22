from funcoes.quiz_funcao import *
from funcoes.banco import *


while True:
    linha()
    print('Quiz'.center(50))
    linha()
    print('1 - Jogar') # Jogar o quiz
    print('2 - Adicionar quiz!!!') # add um quiz pesonalizado
    print('3 - Cancelar Programa') # fecha programa e banco de dados
    linha()
    while True:
        try:
            opcao = int(input('>>> '))
        except ValueError:
            print(f'\033[1;31mERROR: Apenas numeros\033[m')
        else:
            if opcao in (1 , 2 , 3):
                break
            print('\033[1;31mApenas 1, 2 e 3\033[m')

    if opcao == 1:
        perguntas_quiz()

    elif opcao == 2:
        linha()
        print('CRIE UM QUIZ E ADICIONA NO BANCO DE DADOS')
        linha()
        pergunta = str(input('Pergunta: ')).strip()
        resposta1 = str(input('Resposta A):')).strip()
        resposta2 = str(input('Resposta B):')).strip()
        resposta3 = str(input('Resposta C):')).strip()
        resposta4 = str(input('Resposta D):')).strip()
        linha()
        print('Ex: Resposta certa é a A')
        try:
            while True:
                linha()
                resposta_certa = input('Qual é a resposta correta?: ').upper().strip()            
                if resposta_certa in ('A','B','C','D'):
                    break
                print('\033[1;31mERROR: Somente: A, B, C e D!!!\033[m')
            add_dados(pergunta = pergunta , r1 = resposta1 , r2 = resposta2 , r3 = resposta3 , r4 = resposta4, certa = resposta_certa)
        except sqlite3.Error as error:
            print(error)
        else:
            linha()
            print('\033[1;32mQuiz adicionado!!!\033[m')
    
    elif opcao == 3:
        dados.close()
        break