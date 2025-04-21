import reflex as rx
from reflextest.components.navbar import navbar
from reflextest.components.footer import footer
from reflextest.views.header.header import header
from reflextest.views.links.links import links
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos import Size as Size  # usar Size Directo de nuesta fuente de stilos.py
from reflextest.comsensybd.combd import Comunicacion as Combd
from reflextest.comsensybd.classSockClientToEsp8266 import SockClientEsp8266 as sockEsp
from reflextest.stilos.colors import Color as color
import sqlite3


class State(rx.State):
    pass

#def index2()-> rx.Component:
   #eturn rx.text("Hola estamos Reflex co Pytho para Web", color="blue")


def index2()-> rx.Component:
    return rx.box(
        navbar(),
            rx.center(
                 rx.vstack(
                    header(),
                    links(),
                    max_width=stilos.MAX_WIDTH,
                    width="100%",
                    align="center",
                    justify="center",
                    margin_y=Size.BIG.value  #SMALL, DEFAULT, BIG los defini en mis stilos.py
            
                    #background="green"a
                
                 )      
            ),
        footer()   
    )

def index()-> rx.Component:
    datos= Combd() # Crea una Instancia de la clase Comdb (Comunicacion) para interactuar con la base de Datos
    leerEspActul=sockEsp() # Crea una Instacia de la clase SocketClientToEsp para comunicarse con el Sensor
    leerEspActul.ActuaDataEsp8266()  
    #namesdb=datos.get_tables("database.db")
    datosdb=datos.mostrar_datos_fin(5)  #[(id,fecha,hora,temp,hum),[(id,fecha,hora,temp,hum)] (5) pide  los 5 Ultimos datos
    columnasName=datos.get_columnas("tabla_datos") # << Nombre la tabla. Ya en la Clase Comunicacion esta configurado el Nombre de la DB
    #print(columnasName)
    return rx.box(
        navbar(),
            rx.center(
                 rx.vstack( #1
                    header(),
                    links(),
                        rx.vstack( #2
                            rx.heading("Datos base de datos", size="4"),
                            ######### muy buena  #####################
                            rx.hstack(
                                rx.foreach( columnasName,
                                            lambda col: rx.box(
                                            rx.text(col),
                                            padding="0.5em",
                                            border="1px solid black"))),
                            #############################################
                            rx.hstack(  #hstack2

                               rx.list(*[rx.list_item(data[0]) for data in datosdb],  #namesdb cambie por datosdb
                               spacing="sm"),
                               rx.list(*[rx.list_item(data[1]) for data in datosdb],  #namesdb cambie por datosdb
                               spacing="sm"),
                               rx.list(*[rx.list_item(data[2]) for data in datosdb],  #namesdb cambie por datosdb
                               spacing="sm"),
                               rx.list(*[rx.list_item(data[3]) for data in datosdb],  #namesdb cambie por datosdb
                               spacing="sm"),
                               rx.list(*[rx.list_item(data[4]) for data in datosdb],  #namesdb cambie por datosdb
                               spacing="sm"),
                               spacing="7"
                                                      
                            ),# hstack2
                        #deco vstack2
                        bg=color.CONTENT.value,
                        margin=Size.Medium.value,
                        padding=Size.DEFAULT.value,
                        border_radius=Size.DEFAULT.value,
                        ),
                    #deco vstack1        
                    max_width=stilos.MAX_WIDTH,
                    width="100%",
                    align="center",
                    justify="center",
                    margin_y=Size.BIG.value  #SMALL, DEFAULT, BIG los defini en mis stilos.py
                    #background="green"a
                
                 )#vstack1
                 
            ), #center
        footer()   
    )#box1
datos= Combd()
namesdb=datos.get_tables("database.db")
#print(namesdb)
#print("Sr Johnnsson")
app= rx.App(
    style=stilos.BASE_STYLE
)
app.add_page(index)
app._compile()
