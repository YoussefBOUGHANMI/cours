import streamlit as st



def ft_orange():
    
    st.title("🍊 Orange Data Mining")

    st.markdown("""
    **Orange** est un outil gratuit et visuel pour l’analyse de données et le machine learning.  
    Il fonctionne par **glisser-déposer**, sans besoin de coder.

    ---

    ### 🔍 À quoi ça sert ?
    - Explorer les données
    - Créer des modèles prédictifs
    - Visualiser les résultats facilement

    ---

    ### 🎓 Pourquoi en cours ?
    Simple, pédagogique, et parfait pour comprendre les bases de la data science.

    ---

    """)
    
        # Ajout d'un lien vers un site externe avec un style de bouton personnalisé
    st.markdown(
            """
            <style>
            .btn-custom {
                display: inline-block;
                padding: 12px 24px;
                margin: 8px 0;
                border-radius: 4px;
                background-color: FFA500; /* Couleur de fond du bouton */
                color: black;             /* Couleur du texte */
                text-decoration: none;    /* Retire le soulignement du lien */
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            .btn-custom:hover {
                background-color: #FFA500; /* Couleur du bouton au survol */
            }
            </style>

            <a class="btn-custom" href="https://orangedatamining.com/download/" target="_blank">Télecharger orange data mining</a>
            """,
            unsafe_allow_html=True
        )

