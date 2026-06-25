from src.config import REPORT

def gerar_relatorio(dados_processados, emails, sites, datas_formato_invalido, datas_inexistentes, telefone_ramal):
    with open(REPORT, "w", encoding="utf-8") as arquivo:
        arquivo.write("="*30 + "\n")
        arquivo.write("RELATÓRIO DE PROCESSAMENTO\n")
        arquivo.write("="*30 + "\n")
        arquivo.write(f"Total de registros: {len(dados_processados)}\n")
        arquivo.write(f"E-mails inválidos: {len(emails)}\n")
        arquivo.write(f"Sites inválidos: {len(sites)}\n")
        arquivo.write(f"Datas com formato inválido: {len(datas_formato_invalido)}\n")
        arquivo.write(f"Datas inexistentes: {len(datas_inexistentes)}\n")
        arquivo.write(f"Telefones com ramal: {len(telefone_ramal)}\n")
        arquivo.write("="*30 + "\n")