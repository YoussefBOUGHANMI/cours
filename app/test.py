import streamlit as st
from challenge import *
from accueil import *
from tp import *

def surprise():
  st.write("Surprise !!!! ")

#pg = st.navigation([Accueil, TP , Challenge])
pg = st.navigation([Accueil, TP , surprise])
pg.run()
