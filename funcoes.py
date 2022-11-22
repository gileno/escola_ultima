def consulta_aluno(cursor):

    termo = input("Digite o termo de busca: ")

    sql = '''
    select id, nome, email, data from aluno where nome like ? or email like ?
    '''

    termo = f'%{termo}%'

    resultado = cursor.execute(sql, [termo, termo])

    for aluno in resultado:
        print("ID", aluno[0], "Nome", aluno[1], "Email", aluno[2], "Data", aluno[3])
    

def buscar_aluno(cursor, id):
    sql = '''
    select id, nome, email, data from aluno where id = ?
    '''
    resultado = cursor.execute(sql, [id])

    aluno = None
    for aluno in resultado:
        break
    return aluno
