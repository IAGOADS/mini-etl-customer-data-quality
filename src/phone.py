def remover_caracteres_telefone(lista):
    lista_telefones_padronizados = []
    caracteres_proibidos = ["(", ")", ",", ".", "-"]
    for linha in lista:
        # Copia os dados para não alterar a lista original diretamente
        nova_linha = linha.copy()
        phone1 = nova_linha[7]
        phone2 = nova_linha[8]
        for caractere in caracteres_proibidos:
            phone1 = phone1.replace(caractere, "")
            phone2 = phone2.replace(caractere, "")
        nova_linha[7] = phone1
        nova_linha[8] = phone2
        lista_telefones_padronizados.append(nova_linha)
    return lista_telefones_padronizados

def remover_ramal_telefone(lista):
    lista_telefones_sem_ramal = []
    for linha in lista:
        
        nova_linha = linha.copy()

        phone1 = nova_linha[7]
        phone2 = nova_linha[8]

        posicao_phone1 = phone1.find('x')
        posicao_phone2 = phone2.find('x')

        if posicao_phone1 != -1:
            phone1 = phone1[:posicao_phone1]

        if posicao_phone2 != -1:
            phone2 = phone2[:posicao_phone2]

        nova_linha[7] = phone1
        nova_linha[8] = phone2
        lista_telefones_sem_ramal.append(nova_linha)
    return lista_telefones_sem_ramal

def quantificar_ramal(lista):
    linhas_com_ramal = []
    for indice, linha in enumerate(lista):
        telefone1 = linha[7]
        telefone2 = linha[8]
        # Corrigido: para achar ramal, find() deve ser diferente de -1
        if telefone1.find("x") != -1 or telefone2.find("x") != -1:
            linhas_com_ramal.append(indice)
    return linhas_com_ramal

def padronizar_telefone(lista):
    lista_telefone_sem_caracter = remover_caracteres_telefone(lista)
    lista_telefone_padronizado = remover_ramal_telefone(lista_telefone_sem_caracter)
    return lista_telefone_padronizado