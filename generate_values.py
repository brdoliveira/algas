import time
import pandas as pd
from use_db import *

def get_dBA() -> None:
    """
    Função responsável por pegar apenas a coluna 'dBA' depois salvar em um arquivo .csv separado.

    Args:
        none
    Returns:
        none

    Notes:
        dBA: dB representa decibéis e é uma unidade de medida de som. Esta unidade mede a intensidade de um som
        ou a força de um sinal. 
    See: https://www.ehow.com.br/diferencas-entre-dba-dbc-info_41877/
            https://iot.fvh.fi/opendata/noise/
    """
    data = pd.read_csv('./data/LAeq-2020-all.csv')
    getDBA = data['dBA']
    getDBA.to_csv('./data/dBA.csv')

def insert_dBA_BD(name) -> None:
    """
    Função responsável por gerar um valor aleatório e salvar no banco de dados.

    Args:
        none
    Returns:
        none
    """
    create_table()
    dataDBA = pd.read_csv('./data/dBA.csv')

    n_samples : int = 10

    while True:

        start_time_for = time.time()
        for _ in range(50):
            start_time = time.time()
            
            sample = dataDBA['dBA'].sample(n_samples).mean()

            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time = round(elapsed_time, 4)

            insert_table(
                value = float(sample),
                time_used= float(elapsed_time) 
            )
  
        end_time_for = time.time()
        elapsed_time_for = end_time_for - start_time_for
        elapsed_time_for = round(elapsed_time_for,4)

        insert_spend_process(name,elapsed_time_for)

insert_dBA_BD("LOCAL")