import reflex as rx
import reflextest.stilos.stilos as stilos

def title(text: str)-> rx.Component:
    return  rx.heading(
            text,
            size="5",
            style=stilos.title_style
    )