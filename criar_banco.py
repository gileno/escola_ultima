import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql_aluno = '''
CREATE TABLE aluno (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
	"data" TEXT(10),
	email TEXT(100)
)
'''

sql_professor = '''
CREATE TABLE professor (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
	email TEXT(100),
	cpf TEXT(11) NOT NULL
)
'''
cursor.execute(sql_aluno)
cursor.execute(sql_professor)
conexao.commit()
conexao.close()
