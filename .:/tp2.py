import streamlit as st

def tp2_page():
    st.title("🧪 TP2 : Analyse de Commentaires YouTube – Publicité BMW")

    [st.write("\n") for _ in range(2)]

    # Lien vers la vidéo YouTube de la publicité BMW
    st.markdown("📺 **Vidéo de la publicité BMW utilisée dans ce TP :**")
    st.video("https://www.youtube.com/watch?v=9rx7-ec0p0A")

    [st.write("\n") for _ in range(2)]

    
    st.markdown("""
    Dans ce TP, nous allons plonger au cœur des **réactions des internautes** face à une publicité de la marque **BMW** diffusée sur YouTube.  
    Objectif : comprendre la perception de la marque, les émotions exprimées, et les thématiques abordées par les spectateurs.

    ---
    """)

    st.subheader("🔧 Étapes et Outils d'Analyse")

    st.markdown("""
    ### 1. **Exploration des données avec Orange Data Mining**
    - Chargement des commentaires extraits de YouTube
    - Visualisation des fréquences, nuages de mots, clustering simple
    - Analyse rapide et intuitive grâce aux blocs visuels d’Orange

    ### 2. **Analyse Sentimentale avec Voyant Tools**
    - Identification des tonalités positives, neutres et négatives
    - Visualisation de l’évolution émotionnelle dans les commentaires
    - Extraction de phrases clés liées aux sentiments dominants

    ### 3. **Analyse avancée avec un modèle LLM custom (DeepSeek-based)**
    - Modèle de type LLM entraîné sur corpus marketing et commentaires sociaux
    - Analyse de sentiment contextuelle, détection de sous-entendus
    - Lecture "entre les lignes" grâce à une compréhension fine du langage

    ---
    """)

    st.markdown("""
    🧠 **À la fin de ce TP**, vous serez capables de :
    - Utiliser plusieurs outils complémentaires d’analyse de texte
    - Distinguer ce que chaque outil peut apporter selon le niveau d’analyse souhaité
    - Appliquer une démarche d’analyse complète, du brut au sens caché

    👉 Restez curieux, testez différentes visualisations, et comparez les résultats obtenus par chaque outil.
    """)

    st.markdown("---")
    
    # Téléchargement du fichier Excel des commentaires
    try:
        with open("commentaires_bmw_youtube.xlsx", "rb") as file:
            st.download_button(
                label="📥 Télécharger les commentaires YouTube (Excel)",
                data=file,
                file_name="commentaires_bmw_youtube.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except FileNotFoundError:
        st.warning("⚠️ Le fichier Excel des commentaires n'est pas encore disponible.")

    st.caption("Ce TP est à visée pédagogique. Les données utilisées sont publiques et destinées à un usage académique uniquement.")

    
    
    