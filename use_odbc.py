import pyodbc
from credentials import *


def conect_odbc():
    conn_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:bd-monitoramento.database.windows.net,1433;Database=bd-monitoramento;Uid='+ email +'@bd-monitoramento;Pwd='+ pswd +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;;'
    conn = pyodbc.connect(conn_string)
    return conn.cursor()


def insert_table(value : float, time_used: float) -> None:
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
    pyodbc.connect()
    try:
        if pyodbc.is_connected():
            mycursor = pyodbc.cursor()

            sql_query = f'INSERT INTO {database}.dados(id,value,time_used,datetime_insert) VALUES (null,{value},{time_used},now())'

            mycursor.execute(sql_query)
            pyodbc.commit()
    except pyodbc.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if pyodbc.is_connected():
            mycursor.close()
            pyodbc.close()

def insert_spend_process(name: str,time_used: float) -> None:
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
    pyodbc.connect()
    try:
        if pyodbc.is_connected():
            mycursor = pyodbc.cursor()

            sql_query = f"INSERT INTO {database}.dados_maquinas(id,name,time_used,datetime_insert) VALUES (null,'{name}',{time_used},now())"

            mycursor.execute(sql_query)
            pyodbc.commit()
    except pyodbc.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if pyodbc.is_connected():
            mycursor.close()
            pyodbc.close()


def get_inserts(columns : str = "*") -> list:
    """
    Função responsável por buscar os valores inseridos na tabela dados.

    Args:
        columns (str, optional) : Colunas que vão ser retornados, o padrão é retornar todas as colunas
    Returns:
        list: Irá retornar os valores adicionados na tabela dados

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    pyodbc.connect()
    try:
        if pyodbc.is_connected():
            mycursor = pyodbc.cursor()

            sql_query = f'SELECT {columns} FROM {database}.dados'
            mycursor.execute(sql_query)

            result = mycursor.fetchall()
            pyodbc.commit()

            return result
    except pyodbc.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if pyodbc.is_connected():
            mycursor.close()
            pyodbc.close()

def get_inserts_data_machine() -> None:
    """
    Função responsável por buscar os valores inseridos na tabela dados.

    Args:
        columns (str, optional) : Colunas que vão ser retornados, o padrão é retornar todas as colunas
    Returns:
        list: Irá retornar os valores adicionados na tabela dados

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    pyodbc.connect()
    try:
        if pyodbc.is_connected():
            mycursor = pyodbc.cursor()

            sql_query = f'SELECT name, avg(time_used) as media FROM {database}.dados_maquinas GROUP BY name'
            mycursor.execute(sql_query)

            result = mycursor.fetchall()
            pyodbc.commit()

            return result
    except pyodbc.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if pyodbc.is_connected():
            mycursor.close()
            pyodbc.close()