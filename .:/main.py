import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from tp import *
from accueil import *
from orange import *
from challenge import *
#from get_comment import *
#from display_llm import *
#from tp2 import *
#from conseil_llm import *

def ft_navbar_user():

    pages = ["Accueil 🏠" , "TP1 💻", "Challenge 🏆" , "Télecharger ODM ⬇️" ]
    styles = {
        "nav": {
            "background-color": "#294889",
            "justify-content": "left",
        },
        "img": {
            "padding-right": "14px",
        },
        "span": {
            "color": "white",
            "padding": "14px",
        },
        "active": {
            "background-color": "white",
            "color": "var(--text-color)",
            "font-weight": "normal",
            "padding": "14px",
        }
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
    }

    page = st_navbar(
        pages,
        styles=styles,
        options=options,
    )
    
        
    if (page == "Accueil 🏠"):
        display_acc()
    if (page == "TP1 💻"):
        tp_display()
    if (page == "Challenge 🏆"):
        display_challenge()
    if (page == "Télecharger ODM ⬇️"):
        ft_orange()   
    #if(page == "TP2 💻"):
    #    tp2_page()
    #if( page == "Comment Extractor 💬"):
    #    display_comment()
    #if(page == "LLM 🤖"):
    #    display_llm()
    #if(page == "Tips LLM ℹ️"):
    #    llm_conseils_page()


ft_navbar_user()