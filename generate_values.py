import time
import pandas as pd
from sys import getsizeof
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

def insert_dBA_BD() -> None:
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

    for _ in range(1000):
        start_time = time.time()
        
        sample = dataDBA['dBA'].sample(n_samples).mean()

        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time, 4)

        memory = getsizeof(sample)

        insert_table(
            value = float(sample),
            memory_used= float(memory),
            time_used= float(elapsed_time) 
        )

insert_dBA_BD()