import sqlite3

from funcoes import consulta_aluno

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

consulta_aluno(cursor)

aluno_id = input("Digite o ID do aluno: ")
aluno_id = int(aluno_id)

sql = 'delete from aluno where id = ?'

cursor.execute(sql, [aluno_id])

conexao.commit()

conexao.close()
