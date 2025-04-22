import reflex as rx
from reflextest.components.navbar import navbar
from reflextest.components.footer import footer
from reflextest.views.header.header import header
from reflextest.views.links.links import links
import reflextest.stilos.stilos as stilos
from reflextest.stilos.colors import Color as Color
from reflextest.stilos.stilos import Size as Size  # usar Size Directo de nuesta fuente de stilos.py
from reflextest.views.sponsors.sponsors import sponsor
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
 
    return rx.box(
        navbar(),
            rx.center(
                 rx.vstack( #1
                    header(),
                    links(),
                    sponsor(),
               
                #deco vstack1        
                max_width=stilos.MAX_WIDTH,
                width="100%",
                align="center",
                justify="center",
                margin_y=Size.BIG.value,  #SMALL, DEFAULT, BIG los defini en mis stilos.py
                
                 )#vstack1
                 
            ), #center
        footer()   
    )#box1
app= rx.App(
    stylesheets=stilos.STYLESHEETS,
    style=stilos.BASE_STYLE
)
app.add_page(index,
             title="Ing. Willians J. Sequera",
             description= "Python con Reflex",
             image="icons/avatar.png")
app._compile()
