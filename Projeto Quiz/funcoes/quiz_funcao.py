from funcoes.banco import *
from time import sleep
from random import choice


# Para indentificar o nomes ex: pergunta, a b etc
indentificação = ['Pergunta:', 'A)', 'B)', 'C)', 'D)']
ponto = erradas = 0 # armazenamento de pontos

def linha():
    print('_' * 50)


def perguntas_quiz(quantas_perguntas = 10):
    # aqui voce vai fazer que o usuario responda os quiz e guarder as pontuação e as resposta certa.
    global ponto

    
    indeces_aleatorios = []
    for c in range(0,quantas_perguntas):
        indeces_aleatorios.append(c)
    banco = banco_de_dado() # banco de dados
    for quizzes in range(0, quantas_perguntas):
        perguntas = choice(indeces_aleatorios)
        indeces_aleatorios.remove(perguntas)
        print(perguntas)
        sleep(2)
        linha()
        for posicao, valor in enumerate(banco[perguntas]):
            if posicao not in (5, 6):
                sleep(0.3)
                print(f'{indentificação[posicao]} {valor}' , flush = True)
            if posicao == 5:
                acertos = valor
        while True:       
            try:
                sleep(0.9)
                resposta = str(input('Resposta: ')).upper().strip()
            except ValueError: # Verificação de erro                    
                print('\033[1;31mERROR: Algo deu errado verifique as questoes!!!\033[m')
            else:
                if resposta in ('A', 'B' , 'C' , 'D'):
                    verificação_das_resposta(rp = resposta , certas = acertos)
                    break
                print('\033[1;31mERROR: Algo deu errado verifique as questoes!!!\033[m')
        linha()
    ponto = 0


def verificação_das_resposta(rp , certas):
    # aqui voce vai fazer um sistema de ver se o as resposta inserida entao certa, e retorna as resposta certa e as pontuação
    global ponto
    if rp == certas:
        ponto += 1

def tabela_final():
    linha()
    print('Tabela final'.center(50))
    linha()
    print(f'Acertos: {ponto}')
    print(f'Erradas: {len(banco_de_dado()) - ponto}')
    print(f'Total de Pergunta: {len(banco_de_dado())}')
    linha()

