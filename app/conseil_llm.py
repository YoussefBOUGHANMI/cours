import streamlit as st

def llm_conseils_page():
    st.title("🧠 Conseils pour Utiliser un LLM en Analyse Textuelle")

    st.markdown("""
    Cette page vous guide sur les **bonnes pratiques** pour utiliser efficacement un **modèle de langage (LLM)** dans le cadre d’une **analyse de commentaires textuels** (ex. YouTube, réseaux sociaux, enquêtes, etc.).

    L’objectif est d’**améliorer la qualité des réponses** et de **réduire le coût de traitement**, en concevant des prompts pertinents, clairs et bien ciblés.
    """)

    st.markdown("---")
    st.subheader("📌 Les 5 bonnes pratiques pour créer un excellent prompt")

    conseils = [
        ("🎯 1. Spécifie la tâche clairement",
         "Décris exactement ce que tu veux que le modèle fasse : sentiment, résumé, thème, avis, etc."),
        ("📦 2. Importe un format de sortie",
         "Demande une sortie structurée (JSON, liste, tableau) pour faciliter l’analyse automatique."),
        ("🧠 3. Attribue un rôle au modèle",
         "Commence par 'Tu es un expert en...' pour guider le ton, la précision et la rigueur."),
        ("✂️ 4. Reste concis",
         "Plus le prompt est court et clair, plus la réponse est rapide et fiable."),
        ("🧪 5. Teste ton prompt sur plusieurs cas",
         "Vérifie la robustesse du prompt sur des cas positifs, négatifs, ambigus ou ironiques.")
    ]

    for titre, contenu in conseils:
        st.markdown(f"**{titre}**  \n{contenu}\n")

    st.markdown("---")
    st.success("💡 Astuce : Un bon prompt, c’est comme un bon brief. Moins il laisse place au doute, plus le modèle sera performant.")

    st.caption("Page proposée dans le cadre du cours M1 Marketing – Analyse de commentaires par NLP et IA.")
