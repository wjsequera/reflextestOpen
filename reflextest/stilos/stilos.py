
import reflex as rx
from enum import Enum
from .colors import Color as  Color
from .colors import TextColor as  TextColor
from .fonts import Font as  Font
from .fonts import FontWeight as  FontWeight

# Constantes
MAX_WIDTH= "600px"


STYLESHEETS={
    "https://fonts.googleapis.com/ccs2?family=Poppins:wght@50;800@display=swap"
    "https://fonts.googleapis.com/ccs2?family=Comfortaa:wght@50;800@display=swap"

}
# Sizes

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VBIG="4em"
  
    Small="1"
    Medium="2"
    Default="4"
    Large="8"
    Big="9"
    


#style
BASE_STYLE = {
     "font_family":Font.DEFAULT.value,
     "font_weight":FontWeight.LIGHT.value,
     "background_color":Color.BACKGROUND.value,
     #"background_color":"blue",
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block", #cuando la quito las letras del button link se van al centro
        #"white_space":"normal",
        "text_align":"start",
        "padding":Size.SMALL.value,
        "border_radius":Size.SMALL.value,
        "_hover":{"background_color":Color.C_HOVER.value},  #C_HOVER  SECUNDARY
        "background_color":Color.CONTENT.value,             #CONTENT
        "color":TextColor.HEADER.value
        
        #"color":"red"
        #"color":"lightblue"
    },
    rx.link:{
       "font_family":Font.LOGO.value,
       #"text_decoration":"green",
       "text_decoration":"underline",
       #"_hover":{},
       # "_hover":{"color": "red"}
        #"_hover":{"background_color":"green"},
    }
}

navbar_title_style= {
           #"font_family":"https://fonts.google.com/share?selection.family=Codystar:wght@300;2400",
           "font_family":Font.LOGO.value,
           "font_weight":FontWeight.MEDIUM.value,
           #"font_family":"Poppins-Bold",
           #"font_family":"Comfortaa",
           "font_size": Size.BIG.value
}
title_style={
        "font_family":Font.LOGO.value,
        "width":"100%",
        "padding_top":Size.SMALL.value,
        "color":TextColor.HEADER.value
}
button_title_style= {  \
        "color":TextColor.HEADER.value
        
    }

button_body_style= {
        "font_family":Font.DEFAULT.value,
        "font_weight":FontWeight.LIGHT.value,
        "font_size":Size.MEDIUM.value,
        "color":TextColor.BODY.value
    }