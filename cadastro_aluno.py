import sqlite3

from datetime import date

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
data = date.today()
data = f'{data.year}{data.month}{data.day}'
sql = '''
insert into aluno (nome, email, data) values (?, ?, ?)
'''
valores = [nome, email, data]
cursor.execute(sql, valores)

conexao.commit()
conexao.close()
