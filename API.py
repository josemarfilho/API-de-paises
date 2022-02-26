import json

import requests

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name/'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisicao', url)
    return None

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer o parsing')


def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


def mostrar_populacao(nome_do_pais):
    resposta = lista_de_paises = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
        else:
            print('Pais nao encontrado')


def mostrar_moedas(lista_de_moedas):
    resposta = lista_de_paises = requisicao('{}/{}'.format(URL_NAME, lista_de_moedas ))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('Moedas do', pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
        else:
            print('Pais nao encontrado')


if __name__ == '__main__':
    print('>>>> Bem-vindo ao sistema de paises')
    print('uso python paises.py <acao> <nome do pais>')
    print('acoes disponiveis: Mostrar moedas, contagem de populacao, contagem de paises ')
