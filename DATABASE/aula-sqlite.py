import sqlite3

#conexão, cursor - ponte, alguém pra trazer e levar.

conexao = sqlite3.connect('Meu primeiro banco.db')
cursor = conexao.cursor()

#Criar tabela - C
# cursor.execute('CREATE TABLE IF NOT EXISTS frutas('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'#PRIMARY KEY - NÃO REPETE / AUTOINCREMENT (VAI AUMENTAR SOZINHO E CREESCENTE)
#                'nome_fruta TEXT,'
#                'variedade TEXT)')

#Inserir dados na tabela - C
#se vai escrever algo em SQL, cursor.execute
cursor.execute('INSERT INTO frutas(nome_fruta, variedade)'
               'VALUES ("Banana", "Caturra")')

#Buscar dados - R
# cursor.execute('SELECT * FROM frutas')
# for fruta in cursor.fetchall():
#     print(f'{fruta[0]} - {fruta[1]} - {fruta[2]}')

#Atualizar registro - U
# cursor.execute('UPDATE frutas SET variedade="Branca" WHERE id=2')


#Deletar - D:
# cursor.execute('DELETE FROM frutas')
cursor.execute('SELECT * FROM frutas')

for fruta in cursor.fetchall():
    print(f'{fruta[0]} - {fruta[1]} - {fruta[2]}')


#Detelar tabela - D
# cursor.execute('DROP TABLE frutas')



conexao.commit()


cursor.close()
conexao.close()
