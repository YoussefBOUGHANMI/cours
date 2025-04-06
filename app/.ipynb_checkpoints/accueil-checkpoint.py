import streamlit as st






def display_acc():

    # Titre principal
    st.title("🎓 Bienvenue sur le site du cours : Maitrise logiciels de traitement de données")
    
    [st.write("\n") for i in range(5)]

    # Message d'accueil
    st.markdown("""
    Bienvenue à toutes et à tous ! 👋  
    Ce site vous accompagnera tout au long de notre cours sur le **Score d’Appétence**, un outil de data science au service du marketing.""")
    
    [st.write("\n") for i in range(4)]

    st.write("""
    > 🧠 L’objectif : comprendre comment prédire l’intérêt potentiel d’un client pour une offre, grâce à des données et des modèles statistiques.""")
    
    [st.write("\n") for i in range(4)]

                
    st.write("""           

    🔍 Vous y trouverez des ressources, et des supports pour approfondir la démarche.

    Bonne exploration !
    """)
    
    st.markdown("---")
    
        # Téléchargement du PowerPoint
    with open("Le-Score-dAppetence-Optimiser-vos-Strategies-Commerciales.pptx", "rb") as file:
        st.download_button(
            label="📥 Télécharger le support de cours (PowerPoint)",
            data=file,
            file_name="Score_Appetence_Cours.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
    
    
    
    
    
    # Pied de page
    st.markdown("---")
    st.caption("Ce site est réservé aux étudiants du cours. Merci de ne pas le diffuser sans autorisation.")
