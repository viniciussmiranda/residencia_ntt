import pandas as pd
import os
import chardet

def verificar_encoding(arquivo):
    """Verifica o encoding do arquivo."""
    with open(arquivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']

def converter_csv(arquivo, encoding='latin1'):
    """Converte o CSV para um DataFrame e organiza os dados."""
    # Verifica o encoding do arquivo
    encoding_atual = verificar_encoding(arquivo)
    print(f'Encoding atual de {arquivo}: {encoding_atual}')
    
    # Lê o CSV com o encoding apropriado
    df = pd.read_csv(arquivo, encoding=encoding_atual)
    
    # Aqui você pode adicionar a lógica para organizar os dados
    # Exemplo: df = df.sort_values(by='coluna_de_interesse')
    
    return df

def salvar_csv(df, nome_arquivo):
    """Salva o DataFrame em um novo arquivo CSV."""
    df.to_csv(nome_arquivo, index=False)

def main():
    arquivos = ['notas_fiscais.csv', 'pedidos.csv']  # Nomes dos seus arquivos CSV
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            df = converter_csv(arquivo)
            # Salva a planilha convertida
            novo_nome = f'convertido_{arquivo}'
            salvar_csv(df, novo_nome)
            print(f'Arquivo {arquivo} convertido e salvo como {novo_nome}')
        else:
            print(f'Arquivo {arquivo} não encontrado.')

if __name__ == "__main__":
    main()
