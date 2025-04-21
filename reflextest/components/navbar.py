import reflex as rx
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos import Size as Size
from reflextest.stilos.colors import Color as Color

def navbar()-> rx.Component:
    return rx.hstack(
                rx.text("WILLIANS",color=Color.PRIMARY.value),
                rx.text("J. SEQUERA",color=Color.SECONDARY.value),
                style=stilos.navbar_title_style,
             position="sticky",  
             bg=Color.CONTENT.value, #"orange",
             padding_x=Size.DEFAULT.value,
             padding_y=Size.SMALL.value,
             z_index="999",
             top="0",   # fila la barr Arrinba
             #Ancho
             flex_direction="row",
             width="100%",
             spacing="2",
        )