import pandas as pd
import os
import glob
from utils_log import log_decorator

@log_decorator
def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator
def calculo_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
def carregar_dados(df: pd.DataFrame, formato_saida: str): 
    if formato_saida == 'csv':
        df.to_csv("dados.csv", index=False)
    elif formato_saida == 'parquet':
        df.to_parquet("dados.parquet", index=False)

@log_decorator
def executar_pipeline(pasta: str, formato_saida: str):
    dados = extrair_dados(path=pasta)
    dados_com_total = calculo_total_vendas(dados)
    carregar_dados(dados_com_total, formato_saida)

if __name__ == "__main__":
    pasta_argumento = 'data'
    formato_saida = 'csv'  # ou 'parquet'
    executar_pipeline(pasta_argumento, formato_saida)
