import sqlite3

conexao = sqlite3.connect('banco_pokemon.db')
cursor = conexao.cursor()


# PARA ADICIONAR UM POKÉMON:
def adicionarPokemon(nome, tipo, pokedex, level=1):
    cursor.execute('INSERT INTO lista_pokemons(nome, tipo, pokedex, level)'
                   'VALUES(?,?,?,?)', (nome, tipo, pokedex, level))

# PARA MODIFICAR UM POKÉMON:
def editarPokemon(table, atributoChave, atributoValor, id):
    cursor.execute(f'UPDATE {table} SET {atributoChave}={atributoValor} WHERE id={id}')


# #CONSULTAR LISTA POKÉMON:
def listarPokemons():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'{pokemon[0]} - {pokemon[1]} - {pokemon[2]} - {pokemon[3]}, {pokemon[4]}')

# fz antes perguntar dps p ativar o deletar
# PARA DELETAR UM POKÉMON:
def deletarPokemon(nome):
    certeza = input('Tem certeza? S/N').upper()
    if certeza == 'S':
        cursor.execute(f'DELETE FROM lista_pokemons WHERE nome="{nome}"')

def evoluirPokemon(nome, evolucao):
    cursor.execute(f'UPDATE lista_pokemon SET nome={evolucao} WHERE nome={nome}')

# TESTE ------------------ ADC
# adicionarPokemon('Eevee', 'Normal', '133', 7)

# TESTE ------------------ LISTAR
listarPokemons()

# TESTE ------------------ ALTERAR
# editarPokemon('lista_pokemons', 'level', 44, 3)
# listarPokemons()

# TESTE ------------------- DELETAR
# deletarPokemon('Leafeon')
# listarPokemons()
#

#TESTE --------------------- EVOLUIR
evoluirPokemon()



# - padrão
conexao.commit()

cursor.close()
conexao.close()
