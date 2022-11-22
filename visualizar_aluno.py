import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

termo = input("Digite o termo de busca: ")

sql = '''
select id, nome, email, data from aluno where nome like ? or email like ?
'''

termo = f'%{termo}%'

resultado = cursor.execute(sql, [termo, termo])

for aluno in resultado:
    print("ID", aluno[0], "Nome", aluno[1], "Email", aluno[2], "Data", aluno[3])

conexao.close()
