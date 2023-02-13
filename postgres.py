import psycopg2
import pickle


class Conexion:
    user = ''
    password = ''
    host = ''
    port = ''
    database = ''
    sentencia = ''

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database




    def __str__(self):
        global conex
        global conexion
        global registros
        
        conexion = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
            )
        

        cursor = conexion.cursor()
        sentencia = str(input('Escribe el query: '))
        cursor.execute(sentencia)
        registros = cursor.fetchall()
        
        return 'La consulta se encuentra guardada'


    def guardar_archivo(self):

        file1 = open('prueba.txt', 'wb',)
        pickle.dump(registros, file1)
        file1.close

        
usuario_1 = Conexion('postgres','R3fr3sc0','127.0.0.1','5432','test_db')
print(usuario_1)
usuario_1.guardar_archivo()
