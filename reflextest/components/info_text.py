import reflex as rx
from reflextest.stilos.stilos import Size as Size
from reflextest.stilos.colors import Color as Color
from reflextest.stilos.colors import TextColor as TextColor


def info_text(title:str, body:str)-> rx.Component:
    return rx.box(
                rx.hstack(
                    rx.text(title, 
                            font_weight="bold", 
                            color=Color.PRIMARY.value),
                    rx.text(body, 
                            color=TextColor.BODY.value)  #orange
                ),
                
            font_size=Size.MEDIUM.value,
            width="100%"

    )