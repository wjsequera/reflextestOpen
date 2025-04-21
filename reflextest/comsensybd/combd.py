import reflex as rx
import sqlite3


class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect("database.db")
        cursor = self.conexion.cursor()
        # CODIGO PARA DEFINIR CREAR UNA TABLA SI NO EXISTE
        self.conexion.execute(''' CREATE TABLE IF NOT EXISTS tabla_datos (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FECHA TEXT NOT NULL,
        HORA TEXT NOT NULL,
        TEMPERATURA TEXT NOT NULL,
        HUMEDAD TEXT NOT NULL);  ''')
        print("Tabla Temperatura y Humedad Creada Exitosamente")

    # Funciones para Manipular la Base de Datos

    # def inserta_producto(self, fehca,hora,temperatura, humedad):
    def inserta_datos(self, fecha, hora, temp, humed):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO tabla_datos (FECHA,HORA,TEMPERATURA,HUMEDAD)
        VALUES('{}','{}','{}','{}')'''.format(fecha, hora, temp, humed)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT *FROM tabla_datos"
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_datos(self, nombre_producto):
        # se quiere: "SELECT *FROM tabla_datos WHERE NOMBRE = 'nombre_producto'"
        # se quiere: "SELECT *FROM tabla_datos WHERE NOMBRE = 'laptop1'"
        cursor = self.conexion.cursor()
        bd = "SELECT *FROM tabla_datos WHERE NOMBRE ='" + nombre_producto + "'"
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        return nombreX

    def elimina_datos(self, nombre):
        # se quiere: '''DELETE FROM tabla_datos WHERE NOMBRE = '{}' '''.format(nombre)
        # se quiere: "DELETE FROM tabla_datos WHERE NOMBRE = 'laptop1'"
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM tabla_datos WHERE NOMBRE ='{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualiza_datos(self, id, codigo, nombree, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = '''UPDATE tabla_datos SET CODIGO = '{}', NOMBRE = '{}', MODELO = '{}', PRECIO = '{}',CANTIDAD = '{}' WHERE ID = '{}' '''.format(
            codigo, nombree, modelo, precio, cantidad, id)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def mostrar_datos_fin(self, k):
        # Retorna las ultimas k lineas de la Base de Datos
        n=0
        datoss = self.mostrar_datos()
        dataEnd = []
        # print(datos)
        i = len(datoss)
        ##print(i)
        ##print(datoss[i - 1])
        ##print(k)

        for j in range(i-k, i):
            #print(j)
            dataEnd.append(datoss[j])
        return dataEnd

    def get_tables(self,db_path):
        # Conectar a la base de datos
            #self.conn = sqlite3.connect(db_path)
            #cursor = self.conn.cursor()
        cursor=self.conexion.cursor()
    
        # Obtener la lista de tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
    
        # Cerrar la conexión
                #self.conn.close()
        self.conexion.close()
    
        # Devolver la lista de tablas
        return [table[0] for table in tables]
    
    def get_columnas(self,tabladb):
        cursor=self.conexion.cursor()
        # Obtener lista de Columnas
        #cursor.execute("PRAGMA table_info(clientes)")  # Reemplaza "clientes" por tu tabla
        cursor.execute(f"PRAGMA table_info({tabladb})")
        columnas = cursor.fetchall()
        columnames= [colum[1] for colum in columnas]
        print(columnames)
        return columnames
        # Cerrar la conexión
                #self.conn.close()
        self.conexion.close()
    
        # Devolver la lista de tablas
        





# Press the green button in the gutter to run the script.
#if __name__ == '__main__':       # para corre y usar la clase se descometa y luego se crea una instacia InstA=Comunicacion()
   # A = 1
    # INSTANCIA INICIAL CREA LA CLASE Y LA TABLA SINO EXISTE
    # Comunicacion()
    # SE CREA UNA INSTANCIA DE LA CLASE COMUNICACION (CON LA BASE DE DATOS)
    # PARA PRUEBAS CON LA BASE DE DATOS
    #A = Comunicacion()
    # A.inserta_producto("A0001", "laptop1", "samsung4", "300", "40")
    # A.inserta_producto("A0002", "laptop2", "samsung4", "300", "50")
    # A.inserta_producto("A0003", "laptop3", "samsung4", "300", "60")
    # A.inserta_producto("A0004", "laptop4", "samsung4", "300", "70")
    # print(A.elimina_productos('laptop4'))
    #print(A.mostrar_datos())
    #print(A.mostrar_datos_fin(20))
    ##print(A.busca_producto("laptop3"))
    ##print(A.actualiza_productos('14', 'A00014', 'laptop14', 'samsung14', '314', '64'))
    ##print(A.mostrar_productos())
    ## See PyCharm help at https://www.jetbrains.com/help/pycharm/