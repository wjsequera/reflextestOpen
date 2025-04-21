import reflex as rx
from reflextest.components.navbar import navbar
from reflextest.components.footer import footer
from reflextest.views.header.header import header
from reflextest.views.links.links import links
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos import Size as Size  # usar Size Directo de nuesta fuente de stilos.py
from reflextest.comsensorbd.comunicacionbd import Comunicacion as Combd
import sqlite3


class State(rx.State):
    pass

#def index()-> rx.Component:
#    return rx.text("Hola estamos Reflex co Pytho para Web", color="blue")


def index()-> rx.Component:
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
datos= Combd()
print(datos.get_tables("database.db"))
app= rx.App(
    style=stilos.BASE_STYLE
)
app.add_page(index)
app._compile()
