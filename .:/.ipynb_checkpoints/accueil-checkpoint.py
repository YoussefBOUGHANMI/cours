import streamlit as st




import streamlit as st

def Accueil():
    # Titre principal
    st.title("🎓 Bienvenue sur le site du cours : Traitement de la données")

    [st.write("\n") for _ in range(4)]

    # Message d'accueil
    st.markdown("""
    Bonjour à toutes et à tous ! 👋  
    Ce site vous accompagnera tout au long de notre cours sur le **Traitement Automatique du Langage Naturel (NLP)**, une technologie clé dans la transformation digitale du marketing.
    """)

    [st.write("\n") for _ in range(3)]

    st.write("""
    > 🎯 **Objectif du cours :** Comprendre ce qu’est le NLP, ses applications marketing, et comment l’utiliser pour générer des insights, automatiser des tâches, et personnaliser les interactions client.
    """)

    [st.write("\n") for _ in range(3)]

    st.write("""
    📚 Sur ce site, vous trouverez des ressources complémentaires, des cas d’usage concrets, et bien sûr le support de cours en téléchargement.

    Bonne découverte ! 🚀
    """)

    st.markdown("---")

    # Téléchargement du PowerPoint
    with open("Le-NLP-au-Service-du-Marketing.pptx", "rb") as file:
        st.download_button(
            label="📥 Télécharger le support de cours (PowerPoint)",
            data=file,
            file_name="NLP_Marketing_Cours.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

    # Pied de page
    st.markdown("---")
    st.caption("Ce site est réservé aux étudiants du cours de M1 Marketing. Ne pas diffuser sans autorisation.")

