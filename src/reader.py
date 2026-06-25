import csv

def transformar_arquivo_lista(caminho):
    lista = []
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        for linha in csv.reader(arquivo, delimiter=','):
            lista.append(list(linha))
    return lista