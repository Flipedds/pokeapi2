from flask import Flask
from flask import render_template
from flask import request
import requests
import json

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicial.html')


@app.route('/<poke>')
def mostrar(poke):
    requisicao = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    pokemon = json.loads(requisicao.text)
    id = pokemon['id']
    nome = pokemon['forms'][0]['name']
    tipos = pokemon['types']
    lista_tipos = []
    for tipo in tipos:
        types = tipo['type']['name']
        lista_tipos.append(types)

    hp = pokemon['stats'][0]['base_stat']

    ataque = pokemon['stats'][1]['base_stat']

    defesa = pokemon['stats'][2]['base_stat']

    peso = pokemon['weight'] / 10

    altura = pokemon['height'] / 10

    ataque_especial = pokemon['stats'][3]['base_stat']

    defesa_especial = pokemon['stats'][4]['base_stat']

    velocidade = pokemon['stats'][5]['base_stat']

    foto = pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

    return render_template('teste.html', nome=nome, id=id, hp=hp, ataque=ataque, defesa=defesa,
                           ataque_especial=ataque_especial,
                           defesa_especial=defesa_especial, velocidade=velocidade, foto=foto, lista_tipos=lista_tipos,
                           peso=peso, altura=altura)


@app.route('/pesquisar', methods=['POST'])
def buscar():
    pokemon = request.form.get('buscar')
    try:
        requisicao = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        pokemon = json.loads(requisicao.text)
        id = pokemon['id']
        nome = pokemon['forms'][0]['name']
        tipos = pokemon['types']
        lista_tipos = []
        for tipo in tipos:
            types = tipo['type']['name']
            lista_tipos.append(types)

        hp = pokemon['stats'][0]['base_stat']

        ataque = pokemon['stats'][1]['base_stat']

        defesa = pokemon['stats'][2]['base_stat']

        peso = pokemon['weight'] / 10

        altura = pokemon['height'] / 10

        ataque_especial = pokemon['stats'][3]['base_stat']

        defesa_especial = pokemon['stats'][4]['base_stat']

        velocidade = pokemon['stats'][5]['base_stat']

        foto = pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

        return render_template('teste.html', nome=nome, id=id, hp=hp, ataque=ataque, defesa=defesa,
                               ataque_especial=ataque_especial,
                               defesa_especial=defesa_especial, velocidade=velocidade, foto=foto,
                               lista_tipos=lista_tipos,
                               peso=peso, altura=altura)
    except:
        return render_template('inicial.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)
