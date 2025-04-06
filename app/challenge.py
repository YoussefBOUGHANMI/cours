
import streamlit as st

# --- Configuration de la page ---
st.set_page_config(
    page_title="Maitrise logiciels de traitement de données",
    layout="centered",  # "wide" pour large, "centered" pour centré
)

# --- CSS personnalisé ---
st.markdown("""
    <style>
    /* Titre principal */
    .main-title {
        color: #4B0082; 
        text-align: center;
        font-size: 2.5em; 
        font-weight: bold;
        margin-top: 0;
        margin-bottom: 0.2em;
    }
    /* Sous-titre */
    .subtitle {
        color: #555;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    /* Style pour les sections */
    .section-header {
        color: #4B0082; 
        font-size: 1.5em;
        margin-top: 2em;
        margin-bottom: 0.5em;
    }
    /* Encadré pour mieux séparer les sections */
    .section-box {
        background-color: #f9f9f9;
        padding: 1.5em;
        border-radius: 8px;
        margin-bottom: 1em;
    }
    /* Centrer un peu de marge autour des boutons */
    .download-btn {
        margin-top: 0.5em;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titre & sous-titre de la page ---
st.markdown('<h1 class="main-title">Maitrise logiciels de traitement de données</h1>', unsafe_allow_html=True)


    
    
# --- Section 2 : Challenge ---
st.markdown('<div class="section-header">Challenge</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.write("Deux fichiers sont disponibles pour le **Challenge**.")

    # Création de colonnes pour aligner les boutons côte à côte
    col1, col2 = st.columns(2)

    with col1:
        # Premier fichier Challenge
        with open("cours_market/challenge/data_train.csv", "rb") as file_challenge1:
            st.download_button(
                label="Fichier Challenge 1",
                data=file_challenge1,
                file_name="Challenge_1.csv",
                mime="text/csv",
                key="challenge1_download",
                help="Cliquez pour télécharger le premier fichier du challenge"
            )

    with col2:
        # Deuxième fichier Challenge
        with open("cours_market/challenge/data_train.csv", "rb") as file_challenge2:
            st.download_button(
                label="Fichier Challenge 2",
                data=file_challenge2,
                file_name="Challenge_2.csv",
                mime="text/csv",
                key="challenge2_download",
                help="Cliquez pour télécharger le deuxième fichier du challenge"
            )

    st.markdown('</div>', unsafe_allow_html=True)

# --- Pied de page (facultatif) ---
st.write("")

