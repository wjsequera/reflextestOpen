import reflex as rx
from  reflextest.components.link_button import link_button
from reflextest.components.title import title
from reflextest.stilos.stilos import Size as Size

def links()-> rx.Component:
    return rx.vstack(     
        title("Comunidad"),  
        link_button("Twich","Directos de Lunes a Jueves","https://twitch.tv/mouredev","icons/twitch.svg"),
        link_button("YouTube","Pelis de fin de Semana","https://youtube.com/@mouredev","icons/twitch.svg"),
        link_button("Twitter","Chat de la comunidad","https://youtube.com/@mouredevtv","icons/twitch.svg"),
        
        title("Ambiente"),
        link_button("Twich","Directos de Lunes a Jueves","https://twitch.tv/mouredev","icons/twitch.svg"),
        link_button("YouTube","Pelis de fin de Semana","https://youtube.com/@mouredev","icons/twitch.svg"),
        link_button("Twitter","Chat de la comunidad","https://youtube.com/@mouredevtv","icons/twitch.svg"),
          
           align="center",  # Centra los elementos horizontalmente
           justify="center",  # Centra los elementos verticalmente 
           width="100%",
           #spacing=Size.Medium.value
    )