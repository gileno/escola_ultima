import sqlite3

from funcoes import consulta_aluno

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

consulta_aluno(cursor)

conexao.close()
