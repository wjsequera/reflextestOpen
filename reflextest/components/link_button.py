import reflex as rx
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos  import Size as Size
def link_button(title:str,body:str, url:str,imagen:str)-> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                #rx.icon(tag="arrow_forward"),            
                rx.image(src=imagen,width=stilos.Size.BIG, height=stilos.Size.BIG),
                rx.vstack(rx.text(title,style=stilos.button_title_style),
                          rx.text(body,style=stilos.button_body_style),
                          spacing=Size.Small.value
                )
        
            ),  width="100%"
        ),
        
        href=url,
        is_external=True,
        width= "100%"
    )