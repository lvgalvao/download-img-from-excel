import httpx
import pandas as pd
import time

def converter_para_link_de_download(link_visualizacao):
    """
    Converte um link de visualização do Google Drive em um link de download direto.
    """
    file_id = link_visualizacao.split('/')[-2]
    return f"https://drive.google.com/u/0/uc?id={file_id}&export=download", file_id

def baixar_arquivo(url, destino, tempo_de_espera=0):
    """
    Baixa um arquivo da URL fornecida e salva no destino especificado.
    Se tempo_de_espera for especificado, a função aguardará esse tempo em segundos antes de baixar.
    """
    if tempo_de_espera > 0:
        time.sleep(tempo_de_espera)

    with httpx.stream("GET", url, follow_redirects=True) as resposta:
        if resposta.status_code == 200:
            with open(destino, 'wb') as arquivo:
                for dados in resposta.iter_bytes():
                    arquivo.write(dados)
        else:
            print(f"Falha ao baixar o arquivo: Código de status {resposta.status_code}")

def baixar_arquivos_do_excel(arquivo_excel, coluna_link):
    """
    Lê um arquivo Excel e baixa arquivos a partir de links do Google Drive na coluna especificada.
    Cada arquivo é nomeado usando seu file_id único do link do Google Drive.
    """
    df = pd.read_excel(arquivo_excel)
    for i, linha in df.iterrows():
        link_visualizacao = linha[coluna_link]
        link_download, file_id = converter_para_link_de_download(link_visualizacao)
        nome_arquivo = f"{file_id}.jpeg"  # Modifique a extensão conforme necessário
        baixar_arquivo(link_download, nome_arquivo, tempo_de_espera=1)  # Adicione tempo_de_espera conforme necessário

if __name__ == "__main__":
    # Parâmetros de configuração
    caminho_arquivo_excel = 'data/Teste.xlsx'  # Caminho do arquivo Excel
    coluna_link = 'Link'                                  # Nome da coluna no Excel que contém os links do Google Drive

    # Iniciar o processo de download
    baixar_arquivos_do_excel(caminho_arquivo_excel, coluna_link)
