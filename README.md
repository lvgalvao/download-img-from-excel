# Downloader de Arquivos do Google Drive

Este script Python permite baixar automaticamente arquivos do Google Drive listados em uma coluna de um arquivo Excel.

## Pré-requisitos

Antes de executar este script, você precisa ter Python instalado no seu sistema. Além disso, as bibliotecas `httpx` e `pandas` são necessárias. Você pode instalá-las usando pip:

```bash
pip install -r requirements.txt
```

## Configuração

1. **Arquivo Excel**: Prepare um arquivo Excel com uma coluna contendo links de visualização do Google Drive. Por exemplo, a URL deverá ter o formato `https://drive.google.com/file/d/ID_DO_ARQUIVO/view`.
    
2. **Configurar o Script**: No script Python, atualize as variáveis `caminho_arquivo_excel` e `coluna_link` para refletir o caminho do seu arquivo Excel e o nome da coluna que contém os links, respectivamente.

Nesse exemplo estou colocando o arquivo Excel em uma pasta data e o nome da coluna é Link. 

## Uso

Para usar o script, simplesmente execute-o após configurar o caminho do arquivo Excel e o nome da coluna:

```bash
python main.py
```

O script vai ler cada link no arquivo Excel, converter para um formato de download direto e baixar os arquivos no diretório onde o script está sendo executado.

## Personalização

* **Mudar Local de Salvamento dos Arquivos**: Você pode modificar o script para salvar os arquivos baixados em um diretório específico.
* **Tempo de Espera Entre Downloads**: Se necessário, ajuste o `tempo_de_espera` na função `baixar_arquivo` para adicionar uma pausa entre os downloads.

## Limitações

* O script foi projetado para funcionar com arquivos públicos do Google Drive. Arquivos que requerem permissões especiais podem não ser baixados corretamente.
* A extensão dos arquivos baixados deve ser ajustada manualmente no script, de acordo com o tipo de arquivo que você espera baixar. Estou colocando como padrão .jpeg