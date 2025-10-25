import sqlite3
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade integer NOT NULL,
    email TEXT NOT NULL
                );
''')

'''
cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)",('Maria',25,'aluno@.com'))
cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)",('Vanessa',18,'aluno@.com'))
cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)",('Priscilla',30,'aluno@.com'))

conexao.commit()
conexao.close()
'''

consulta = cursor.execute("SELECT * FROM alunos")
for lista in consulta.fetchall():
    print(f'nome:{lista [1]} - idade: {lista[2]} - email: {lista[3]}')


consulta = cursor.execute("SELECT * FROM alunos where id = 5")
print(f'{consulta}')





cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?", (17,3))
conexao.commit()


cursor.execute("DELETE FROM alunos where id = ?", (9,))
conexao.commit()
conexao.close()