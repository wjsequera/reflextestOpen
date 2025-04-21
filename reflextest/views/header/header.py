import reflex as rx
from reflextest.components.link_icon import link_icon
import reflextest.stilos.stilos as stilos
from reflextest.components.info_text import info_text
from reflextest.stilos.colors import TextColor as TextColor
from reflextest.stilos.colors import Color as Color
from reflextest.stilos.stilos import Size as Size
import reflextest.constants as const
def header()-> rx.Component:
    return rx.vstack(
                rx.hstack(
                         rx.avatar(fallback="WS",
                                   size="8",
                                   color=TextColor.PRIMARYY.value,
                                   src="avatar.png",
                                   padding="2px",
                                   border_color=Color.PRIMARY.value,
                                   radius="full",
                                   border="5px",
                                   bg=Color.PRIMARY.value

                                ),
                         rx.vstack(
                            rx.heading("Willians J. Sequera",
                                       align="left",
                                       color=TextColor.HEADER.value,
                                       style=stilos.navbar_title_style
                                       ),
                            rx.text("@sequerawj", 
                                    color=TextColor.BODY.value,
                                    margin_top="0px",
                                    align="left", 
                                    width="100%"),  #,font_weight="bold"
                            rx.hstack(
                                link_icon(const.SEQUERAWJ),
                                link_icon(const.MOUREDEV_TWICH), 
                                link_icon(const.MOUREDEV_TWICH),
                                ),
                        
                                 align="start", 
                                 justify="center",
                                 width="100%",
                                 #padding="16px"                                
                        
                        ),
                    #justify="center",
                    width="100%",
                    #bg="black"
                    spacing=stilos.Size.Big.value
                    ),
                    rx.flex(
                        info_text("+13", "Anos de Experiencia"),
                        rx.spacer(),
                        info_text("+14", "Tranbajos Propios"),
                        rx.spacer(),
                        info_text("+2", "Programador"),
                        width="100%",
                        align="center"

                ),  

        rx.box(           
        rx.text("""Info: Overriding config value loglevel with env var LOGLEVEL=default Info: Overriding config value frontend_port 
                with env var FRONTEND_PORT=3000 Info: Overriding config value
                sbackend_port with env var BACKEND_PORT=8000")""",
                color=TextColor.BODY.value,
                font_size=Size.MEDIUM.value,
                
                ),
                #width="40%"
                 ),
                align="center",  # Centra los elementos horizontalmente
                justify="center",  # Centra los elementos verticalmente
                width="100%",
                spacing=stilos.Size.Big.value # BIG = "4em" Big="6"
                #spacing=Size.Big.value    # Arriba en la cabezera hay que from reflextest.stilos.stilos import Size as Size
           
                    #align="center"
                      )
    