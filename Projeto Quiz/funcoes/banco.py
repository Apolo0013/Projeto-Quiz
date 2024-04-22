# Importações
import sqlite3
from random import randint



# funções

# essa funcao tem a capacidade de pegear um lista de perguntas e colocar no bancos de dados
def recebervalores(dados_banco):
   for index in range(0 ,len(dados_banco)):
      for posicao , valor in enumerate(dados_banco[index]):
         if posicao == 0:
            perguntas = valor

         if posicao == 1:
            resposta1 = valor

         if posicao == 2:
            resposta2 = valor

         if posicao == 3:
            resposta3 = valor

         if posicao ==  4:
            resposta4 = valor

         if posicao == 5:
            resposta_certa = valor
      add_dados(pergunta = perguntas , r1 = resposta1 , r2 = resposta2 , r3 = resposta3 ,r4 = resposta4 , certa = resposta_certa)

def geradorID():
   global ids_usados
   ids_usados = []
   while True:
      ids = randint(100 , 999)
      if ids not in ids_usados:
         ids_usados.append(ids)
         return ids


def add_dados(pergunta , r1 , r2 , r3 , r4 , certa):
   try:
      cursor.execute(f'INSERT INTO quiz VALUES ("{pergunta}","{r1}","{r2}","{r3}","{r4}","{certa}",{str(geradorID())})')

   except sqlite3.Error as error:
      print(error)
   finally:
      dados.commit()



def Delete_dados(ID):
   # deletação de algum dados
   try:
      cursor.execute(f'DELETE from quiz WHERE ID = {ID}')
   except sqlite3.Error as error:
      print(error)
   finally:
      dados.commit()


def banco_de_dado():
   # ondem irar fica os dados em forma de funcao
   cursor.execute('SELECT * FROM quiz')
   banco = cursor.fetchall()
   return banco

# Programa 'principal'

dados = sqlite3.connect('quizzes.db')
cursor = dados.cursor()


'''try:
   cursor.execute('CREATE TABLE  quiz (pergunta  text , resposta1 text , resposta2 text, resposta3 text , resposta4 text , resposta_certa text , ID integer)')
   dados.commit()
except sqlite3.Error as error:
   print(error)
else:
   print('fds')'''


dados.commit()
