import pyodbc
from credentials import *

def insert_table_odbc(value : float, time_used: float) -> None:
    """
    Função responsável por inserir registro no banco de dados.

    Args: 
        value (float): Valor que será adicionado no banco de dados
        memory_used (float): Memória gasta na execução
        time_used (float): Tempo gasto na execução
    Returns:
        none

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conexao)
    try:
        cursor = conn.cursor()

        sql_query = f'INSERT INTO {database}.dados(value,time_used,datetime_insert) VALUES ({value},{time_used},getdate())'
        print(sql_query)

        cursor.execute(sql_query)
        cursor.commit()
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

def insert_spend_process_odbc(name: str,time_used: float) -> None:
    """
    Função responsável por inserir registro no banco de dados.

    Args: 
        name (str): Nome do servidor que será adicionado no banco de dados
        time_used (float): Tempo gasto na execução
    Returns:
        none

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conexao)
    try:
        cursor = conn.cursor()

        sql_query = f"INSERT INTO {database}.dados_maquinas(name,time_used,datetime_insert) VALUES ('{name}',{time_used},getdate())"
        print(sql_query)

        cursor.execute(sql_query)
        cursor.commit()
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()


def get_inserts_odbc(columns : str = "*") -> list:
    """
    Função responsável por buscar os valores inseridos na tabela dados.

    Args:
        columns (str, optional) : Colunas que vão ser retornados, o padrão é retornar todas as colunas
    Returns:
        list: Irá retornar os valores adicionados na tabela dados

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conexao)
    try:
        cursor = conn.cursor()

        sql_query = f'SELECT {columns} FROM {database}.dados'
        cursor.execute(sql_query)

        result = cursor.fetchall()
        cursor.commit()

        return result
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

def get_inserts_data_machine_odbc() -> None:
    """
    Função responsável por buscar os valores inseridos na tabela dados.

    Args:
        columns (str, optional) : Colunas que vão ser retornados, o padrão é retornar todas as colunas
    Returns:
        list: Irá retornar os valores adicionados na tabela dados

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conexao)
    try:
        cursor = conn.cursor()

        sql_query = f'SELECT name, avg(time_used) as media FROM {database}.dados_maquinas GROUP BY name'
        cursor.execute(sql_query)

        result = cursor.fetchall()
        cursor.commit()

        return result
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()