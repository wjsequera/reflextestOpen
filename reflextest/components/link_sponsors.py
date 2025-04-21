import reflex as rx
import reflextest.stilos.stilos as stilos
from reflextest.stilos.stilos import Size as Size

def link_sponsors(imagen:str, url: str)-> rx.Component:
    return rx.link(
                rx.image(
                  src=imagen,
                  height=Size.VBIG.value,
                  width=Size.VBIG.value,
                ),
            href=url,
            is_external=True,
              ) 