import streamlit as st

def Accueil():
    # Titre principal
    st.title("🎓 Bienvenue sur le site du cours : Data Science & Scores d’Appétence")

    [st.write("\n") for _ in range(4)]

    # Message d'accueil
    st.markdown("""
    Bonjour à toutes et à tous ! 👋  
    Ce site vous accompagnera tout au long de notre cours sur les **scores d’appétence (propensity scoring)**, une approche centrale en data science pour le marketing décisionnel.
    """)

    [st.write("\n") for _ in range(3)]

    st.write("""
    > 🎯 **Objectif du cours :** Comprendre comment construire, interpréter et exploiter des scores d’appétence pour prédire le comportement des clients (achat, churn, clic, conversion), et optimiser les actions marketing.
    """)

    [st.write("\n") for _ in range(3)]

    st.markdown("""
    📊 **Au programme :**
    - Introduction aux scores d’appétence et aux cas d’usage marketing  
    - Préparation et exploration des données  
    - Modélisation (régression logistique, arbres, modèles de ML)  
    - Évaluation des modèles   
    - Activation marketing et prise de décision basée sur les scores  

    📚 Sur ce site, vous trouverez des ressources complémentaires, des cas concrets, et le support de cours en téléchargement.

    Bonne découverte ! 🚀
    """)

    st.markdown("---")

    # Téléchargement du PowerPoint
    with open("/mount/src/cours/app/Score_Appetence_Youssef_Boughanmi.pptx", "rb") as file:
        st.download_button(
            label="📥 Télécharger le support de cours (PowerPoint)",
            data=file,
            file_name="Scores_Appetence_Cours.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

    # Pied de page
    st.markdown("---")
    st.caption("Ce site est réservé aux étudiants du cours de M1 Marketing. Ne pas diffuser sans autorisation.")
