import mysql.connector
from credentials import *

mydb = mysql.connector.connect(
    host= host,
    user=usr,
    password= pswd,
    database= database
)

def create_table() -> None:
    """
    Função responsável por criar a tabela caso não tenha no banco de Dados.

    Args:
        none
    Returns:
        none

    Errors:
        mysql.connector.Error: Erro com a conexão com o banco de dados
    """
    mydb.connect()
    try:
        if mydb.is_connected():
            mycursor =  mydb.cursor()

            create_table = f"""
                CREATE TABLE IF NOT EXISTS dados (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    value FLOAT NOT NULL,
                    time_used FLOAT NOT NULL,
                    datetime_insert DATETIME NOT NULL
                )

                CREATE TABLE IF NOT EXISTS dados_maquinas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name STRING NOT NULL,
                    time_used FLOAT NOT NULL,
                    datetime_insert DATETIME NOT NULL
                )
            """

            mycursor.execute(create_table)
            mydb.commit()
            mydb.close()
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)        


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
    mydb.connect()
    try:
        if mydb.is_connected():
            mycursor = mydb.cursor()

            sql_query = f'INSERT INTO {database}.dados(id,value,time_used,datetime_insert) VALUES (null,{value},{time_used},now())'

            mycursor.execute(sql_query)
            mydb.commit()
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def insert_spend_process(name: str,time_used: float) -> None:
    mydb.connect()
    try:
        if mydb.is_connected():
            mycursor = mydb.cursor()

            sql_query = f'INSERT INTO {database}.dados_maquinas(id,name,time_used,datetime_insert) VALUES (null,{name},{time_used},now())'

            mycursor.execute(sql_query)
            mydb.commit()
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()


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
    mydb.connect()
    try:
        if mydb.is_connected():
            mycursor = mydb.cursor()

            sql_query = f'SELECT {columns} FROM {database}.dados'
            mycursor.execute(sql_query)

            result = mycursor.fetchall()
            mydb.commit()

            return result
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()