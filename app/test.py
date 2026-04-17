import streamlit as st
from challenge import *
from accueil import *
from tp import *
#pg = st.navigation([Accueil, TP , Challenge])
pg = st.navigation([Accueil, TP , st.write("Surprise !!!! ")])
pg.run()
