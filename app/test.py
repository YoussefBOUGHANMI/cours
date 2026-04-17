import streamlit as st
from challenge import *
from accueil import *
from tp import *

def Challenge():
  st.write("Surprise !!!! ")

#pg = st.navigation([Accueil, TP , Challenge])
pg = st.navigation([Accueil, TP , Challenge])
pg.run()
