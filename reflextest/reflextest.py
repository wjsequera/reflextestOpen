import reflex as rx
from reflextest.components.navbar import navbar
from reflextest.components.footer import footer
from reflextest.views.header.header import header
from reflextest.views.links.links import links
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos import Size as Size  # usar Size Directo de nuesta fuente de stilos.py
from reflextest.comsensybd.combd import Comunicacion as Combd
from reflextest.comsensybd.classSockClientToEsp8266 import SockClientEsp8266 as sockEsp
from reflextest.stilos.colors import Color as Color
import sqlite3


class State(rx.State):
    items: list[str] = ["Manzana", "Banana", "Naranja"]
    count: int = 0
    columnasName=[]
    datosdb=[]
    def increment(self):
        self.count += 1
        datos= Combd() # Crea una Instancia de la clase Comdb (Comunicacion) para interactuar con la base de Datos
        leerEspActul=sockEsp() # Crea una Instacia de la clase SocketClientToEsp para comunicarse con el Sensor
        leerEspActul.ActuaDataEsp8266()  
    #          #namesdb=datos.get_tables("database.db")
        self.datosdb=datos.mostrar_datos_fin(3)  #[(id,fecha,hora,temp,hum),[(id,fecha,hora,temp,hum)] (5) pide  los 5 Ultimos datos
        self.columnasName=datos.get_columnas("tabla_datos") # << Nombre la tabla. Ya en la Clase Comunicacion esta configurado el Nombre de la DB
    #         #print(columnasName)

    def decrement(self):
        self.count -= 1
    # data: list = []
    # isLoading: bool = False

    def add_item(self):
        self.items.append("Nuevo Item")  # Modifica el estado
        print("Item agregado!")  # Solo para depuración


def index()-> rx.Component:
    # datos= Combd() # Crea una Instancia de la clase Comdb (Comunicacion) para interactuar con la base de Datos
    # leerEspActul=sockEsp() # Crea una Instacia de la clase SocketClientToEsp para comunicarse con el Sensor
    # leerEspActul.ActuaDataEsp8266()  
    #          #namesdb=datos.get_tables("database.db")
    # datosdb=datos.mostrar_datos_fin(5)  #[(id,fecha,hora,temp,hum),[(id,fecha,hora,temp,hum)] (5) pide  los 5 Ultimos datos
    # columnasName=datos.get_columnas("tabla_datos") # << Nombre la tabla. Ya en la Clase Comunicacion esta configurado el Nombre de la DB
    #         #print(columnasName)
    datosdb2=State.datosdb
    return rx.box(
        navbar(),
            rx.center(
                 rx.vstack( #1
                    header(),
                    links(),
                        rx.vstack( #2
                            rx.heading("HOME DATA: Temperatura y Humedad", size="4"),
                            ######### muy buena  #####################
                            rx.hstack(
                                rx.foreach( State.columnasName,
                                            lambda col: rx.box(
                                            rx.text(col),
                                            padding="0.5em",
                                            border="1px solid black"))),
                            #############################################
                            rx.vstack(  #3
                                    rx.foreach( State.datosdb,
                                            lambda col: rx.box(
                                                rx.hstack(
                                                    rx.text(col.to(list)[0]),
                                                    rx.text(col.to(list)[1]),
                                                    rx.text(col.to(list)[2]),
                                                    rx.text(col.to(list)[3]),
                                                    rx.text(col.to(list)[4]),
                                                 #deco hstack   
                                                    spacing="6",
                                                ),
                                        #deco rx,box
                                        margin_y= "1",#Size.SMALL.value, 
                                        padding="0.5em",
                                        border="1px solid black",
                                        width="100%")
                                        ),
                            #deco vstack3
                            width="100%",
                            spacing="1" #espacio vertial entre las cajas (rx.box) de datos
                                 
                                                      
                            ),# vstack3
                    #deco vstack2
                    bg=Color.CONTENT.value,
                    margin=Size.SMALL.value,
                    padding=Size.DEFAULT.value,
                    border_radius=Size.DEFAULT.value,
                    width="100%",
                    spacing="3",  # espacio entre el heading(nombre Bd), nombre de columnas y caja de datos
                    style={                    
                        "_hover": {
                                    
                                    "background_color":Color.CONTENT.value,
                                    "transition": "background-color 1.2s",
                                    "color":Color.SECONDARY.value
                                
                                        }
                        }
                  
                        
                        ), #vstack2
                
                rx.heading(State.count, font_size="2em"),
                rx.button("Increment",
                            color_scheme="grass", 
                            on_click=State.increment,
                         ),
                rx.button("Agregar Item", on_click=State.add_item),
                    
                #deco vstack1 
                spacing="4",          
                max_width=stilos.MAX_WIDTH,
                width="100%",
                align="center",
                justify="center",
                margin_y=Size.BIG.value  #SMALL, DEFAULT, BIG los defini en mis stilos.py
                #background="green"ac
                
                 )#vstack1            
                 
            ), #center
        footer()   
    ) #box1

datos= Combd()
namesdb=datos.get_tables("database.db")
#print(namesdb)
#print("Sr Johnnsson")
app= rx.App(
    style=stilos.BASE_STYLE
)
app.add_page(index)
app._compile()
