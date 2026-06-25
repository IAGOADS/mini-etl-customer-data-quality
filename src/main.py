from src.config import RAW_DATA
from src.reader import transformar_arquivo_lista
from src.cleaning import padronizar_dados, transformar_dates
from src.phone import padronizar_telefone, quantificar_ramal
from src.validation import validar_email, validar_site, validar_dates, validar_datas_existentes
from src.report import gerar_relatorio

def executar_pipeline():
    print("Iniciando o processamento ETL...")
    
    # 1. Extração
    dados_brutos = transformar_arquivo_lista(RAW_DATA)
    
    # 2. Pré-padronização de strings
    dados_limpos = padronizar_dados(dados_brutos)
    
    # 3. Coleta de Métricas/Validações (sobre os dados limpos)
    emails_invalidos = validar_email(dados_limpos)
    sites_invalidos = validar_site(dados_limpos)
    datas_formato_invalido = validar_dates(dados_limpos)
    datas_inexistentes = validar_datas_existentes(dados_limpos)
    telefone_ramal = quantificar_ramal(dados_limpos)
    
    # 4. Transformação Final (Telefones e Tipos de Dados)
    dados_processados = padronizar_telefone(dados_limpos)
    dados_processados = transformar_dates(dados_processados)
    
    # 5. Geração do Relatório
    gerar_relatorio(
        dados_processados, 
        emails_invalidos, 
        sites_invalidos, 
        datas_formato_invalido, 
        datas_inexistentes, 
        telefone_ramal
    )
    
    print("Processamento concluído com sucesso! Relatório gerado na pasta output.")

if __name__ == "__main__":
    executar_pipeline()


#py -m src.main