import pyodbc
from credentials import *

def conect_odbc():
    conn_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:bd-monitoramento.database.windows.net,1433;Database=bd-monitoramento;Uid='+ email +'@bd-monitoramento;Pwd='+ pswd +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;;'
    conn = pyodbc.connect(conn_string)
    return conn.cursor()