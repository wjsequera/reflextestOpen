# Scrip de Python Socket client  Conecta ESP8266 responde con Temp y Hum
# Conexion DIrecta de Aqui Hara una Clase llamada SockClientToEsp8266
# Esta clase ademas de traer y mostrar los Datos en mainui.py tambien se conecta
# a la Base de Datos (pyqt6_bdtemphund) y guarda el dato con la funcion inserta_datos
# que se encuentra al final, esto gracia aque se importo la clase Comunicac de
# conexion_sqlitesEsp  y


from datetime import datetime
import threading, time
import logging
from threading import Thread
import socket
#from conexion_sqliteEsp import Comunicacion  del proyecto Realice Original con QT6
from .combd import Comunicacion  # Clase que se comunica con la Base de Datos sqlite
import reflextest.constants as const  # acceder a las direeciones IP External o Internal como constantes

# create an INET, STREAMing socket
##serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
##serversocket.bind(('', 80))
# become a server socket
# serversocket.listen(5)


class SockClientEsp8266():
    def __init__(self):
        # sensor='S1'
        # datos=(sensor + " No Comunico")
        self.obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.host = '192.168.0.104'
        self.host = const.IP
        self.port = const.PORT
        numsensor = "1"
        self.base_datos = Comunicacion()
        try:
            self.fechahora = datetime.now()
            self.obj.connect((self.host, self.port))
            self.obj.settimeout(10)
            # print("Conectado al servidor Esp8266 " )
            self.obj.send(b'mensajeWJS')
            # update.message.reply_text("Mensaje Enviado al S2  ESP32")
            self.datos = self.obj.recv(4096)
            # print(datos)  b'TempS: 27.4 C HumS 61.2'
            self.datosEsp8266 = str(self.datos.decode())  # TempS: 27.4 C HumS 61.2
            # print(self.datosEsp8266)
            self.obj.close()
            self.fechahoraStr = str(self.fechahora)
            self.fechahoracorta = self.fechahoraStr.split(".")
            self.fh = self.fechahoracorta[0]
            # print("Conexión con el Sensor " + sensor + " cerrada")
            # return()  retorna
        except OSError as e:
            print('Falla:' + str(e))

    def leerEsp(self):
        self.obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = const.IP
        self.port = const.PORT
        try:
            self.fechahora = datetime.now()
            self.obj.connect((self.host, self.port))
            self.obj.settimeout(10)
            # print("Conectado al servidor Esp8266 " )
            self.obj.send(b'mensajeWJS')
            # update.message.reply_text("Mensaje Enviado al S2  ESP32")
            self.datos = self.obj.recv(4096)
            # print(datos)  b'TempS: 27.4 C HumS 61.2'
            self.datosEsp8266 = str(self.datos.decode())  # TempS: 27.4 C HumS 61.2
            # print(self.datosEsp8266)
            self.obj.close()
            self.fechahoraStr = str(self.fechahora)
            self.fechahoracorta = self.fechahoraStr.split(".")
            self.fh = self.fechahoracorta[0]
            # print("Conexión con el Sensor " + sensor + " cerrada")
            # return()  retorna
        except OSError as e:
            print('Falla:' + str(e))

    def ActuaDataEsp8266(self):
        # lsita a Usar
        dataesp: list = ["", "", "", "", ]
        ffhh: list = ["", "", ]
        temphum: list = ["", "", ]

        # leo para Actualizar
        self.leerEsp()
        # proceso fecha y hora de Registro
        ffhh = self.fh.split(" ")
        # print(ffhh)
        dataesp[0] = ffhh[0]
        dataesp[1] = ffhh[1]
        # proceso data del sensor de temperatura y humedad conectado al esp8266
        datoss = self.datosEsp8266
        temphum = datoss.split(" ")  # Con este Split la dat se divide en 5 Partes
        # print(temphum[1])
        dataesp[2] = str(temphum[1])     # TempS: 27.4 C HumS 61.2
        dataesp[3] = str(temphum[4])     # pat1  /pat2 /3 /4   /5
        # Guarda la Data en Base de Datos
        fechaa = dataesp[0]
        horaa = dataesp[1]
        tempp = dataesp[2]
        humedd = dataesp[3]
        # INSERTA DATA RECIBIDA DEL ESP EN LA BASE DE DATOS
        self.base_datos.inserta_datos(fechaa, horaa, tempp, humedd)
        # RETURNA LA DATA RECIBIDAD EL ESP A LA VENTA QUE LA MUESTRA
        return dataesp


# def main() -> None:
#    while True:
#        testSock= SockClientEsp8266()
#        print(testSock.datosEsp8266)
#        time.sleep(2)

#if __name__ == '__main__':    # Se activa se se va usar la clase y ver resultados aqui mismo
    # Ejemplo de Uso de la Clase
    #A = SockClientEsp8266()
    #print(A.datosEsp8266)  # temperatura y Humedad juntos
    #A.ActuaDataEsp8266() ## Datos del ESP y lo guarda en la BD
    #while True:
        #datosEsp = A.ActuaDataEsp8266()
        #datosEsp.ActuaDataEsp8266()
        ##print("fecha: %s" % datosEsp[0])  # fecha
        ##print("hora: %s" % datosEsp[1])  # hora
        ##print("temperatura: %s" % datosEsp[2])  # temperatura
        ##print("humedad: %s" % datosEsp[3])  # humedad
        # print(A.humedad())     # Humedad
        # print(A.fechaHoraReg())# Fecha y hora cuando se registro el Dato
        # print(A.fechaReg())    # Fecha cuando se registr el Dato
        # print(A.horaReg())     # Hora cuando se registr el Dato

    # main()
