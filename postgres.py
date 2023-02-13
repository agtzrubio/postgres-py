import psycopg2
import pandas as pd
from sqlalchemy import create_engine, URL, text

 

class Inst:
    
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database



    def __str__(self):
        global con


        url_object = URL.create(
        "postgresql",
        username=self.username,
        password=self.password,  # plain (unescaped) text
        host=self.host,
        port=self.port,
        database=self.database,
                )
        engie = create_engine(url_object)
        con = engie.connect()

        return 'Conexion Establecida'

    def guardarArchivo(self):
        table_df = pd.read_sql_table(table_name='persona',con=con)     
        table_df.to_csv('prueba.csv', index=False, sep=';')


persona1 = Inst('postgres','R3fr3sc0','127.0.0.1','5432','test_db')
print(persona1)
persona1.guardarArchivo()
