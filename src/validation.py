import re

def validar_email(lista):
    lista_indice_emails_invalidos = []
    for indice, linha in enumerate(lista):
        email = linha[9] 
        if '@' not in email or email == "":
            lista_indice_emails_invalidos.append(indice)
    return lista_indice_emails_invalidos

def validar_site(lista):
    site_invalidos = []
    for indice, linha in enumerate(lista):
        site = linha[11]
        if "https://" not in site and "http://" not in site:
            site_invalidos.append(indice)
    return site_invalidos

def validar_dates(lista):
    dates_invalidas = []
    for indice, linha in enumerate(lista):
        dates = linha[10]
        if dates == "" or not(re.fullmatch(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", dates)):
            dates_invalidas.append(indice)
    return dates_invalidas

def validar_datas_existentes(lista):
    meses = [["01",31],["02",29],["03",31],["04",30],["05",31],["06",30],["07",31],["08",31],["09",30],["10",31],["11",30],["12",31]]
    dates_inexistentes = []
    for indice, linha in enumerate(lista):
        dates = linha[10]
        # Evita quebrar o código caso a string da data esteja vazia ou menor que o esperado
        if len(dates) < 10:
            continue
        mes = dates[5:7]
        dia = int(dates[8:])
        for linha_mes in meses:
            mes_espc, quant_dias = linha_mes
            if mes_espc == mes:
                if dia > quant_dias:
                    dates_inexistentes.append(indice)
    return dates_inexistentes