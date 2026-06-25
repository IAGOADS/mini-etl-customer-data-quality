from datetime import date
from src.validation import validar_dates, validar_datas_existentes

def padronizar_dados(lista):
    dados_limpos = []
    for indice, linha in enumerate(lista):
        if indice == 0: 
            continue
        index, id, first_name, last_name, company, city, country, phone1, phone2, email, dates, site = linha
        
        nova_linha = [
            int(index.strip()),
            id.strip(),
            first_name.title().strip(),
            last_name.title().strip(),
            company.title().strip(),
            city.title().strip(),
            country.title().strip(),
            phone1.strip(),
            phone2.strip(),
            email.strip(),
            dates.strip(),
            site.strip()
        ]
        dados_limpos.append(nova_linha)
    return dados_limpos

def transformar_dates(lista):
    datas_sem_padrao = validar_dates(lista)
    indices_linhas_dates_invalidas = validar_datas_existentes(lista)
    dados_atualizados_datas_padrao = []

    if len(indices_linhas_dates_invalidas) == 0 and len(datas_sem_padrao) == 0:
        for linha in lista:
            nova_linha = linha.copy()
            nova_linha[10] = date.fromisoformat(nova_linha[10])
            dados_atualizados_datas_padrao.append(nova_linha)
        return dados_atualizados_datas_padrao
    return lista  # Retorna a lista original se houver erros de data