import streamlit as st
import pandas as pd
import requests
import io
import asyncio
import aiohttp
import ssl


# 🔐 Configuration
DEEPSEEK_API_KEY = "sk-27a8039f6aa9440985ab9009a1fc5eca"
PROTECTED_PASSWORD = "prof123"  # à personnaliser
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"
MAX_COMMENTS = 1000


# === Fonction pour interroger DeepSeek ===
def ask_deepseek(prompt, comment):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": f"{prompt}\n\nCommentaire : {comment}"}
        ],
        "temperature": 0.2
    }
    try:
        response = requests.post(DEEPSEEK_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Erreur: {e}"



# Async version de l’appel à DeepSeek
async def async_ask_deepseek(session, prompt, comment):
    
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": f"{prompt}\n\nCommentaire : {comment}"}
        ],
        "temperature": 0.2
    }
    try:
        async with session.post(DEEPSEEK_URL, headers=headers, json=payload) as response:
            data = await response.json()
            return data['choices'][0]['message']['content']
    except Exception as e:
        return f"Erreur: {e}"

# Fonction qui gère tous les appels asynchrones avec barre de progression
async def process_all_comments(comments, prompt):
    results = []
    progress_bar = st.progress(0)
    total = len(comments)


    # Créer un contexte SSL qui ignore les vérifications (pour contourner l'erreur SSL)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    connector = aiohttp.TCPConnector(limit=50, ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [async_ask_deepseek(session, prompt, str(comment)) for comment in comments]

        for i, coro in enumerate(asyncio.as_completed(tasks)):
            result = await coro
            results.append(result)
            progress_bar.progress((i + 1) / total)

    return results

  

    
def display_llm():
    # === Interface Streamlit ===
    st.title("🧠 LLM Prompt Lab & Analyse des Commentaires")

    # ----------------------
    # 1️⃣ Zone libre - Test de prompt
    # ----------------------
    st.header("🔍 1. Tester un prompt")

    with st.form("test_form"):
        prompt = st.text_area("✍️ Prompt fermé (ex: Est-ce que ce commentaire est négatif ou positif ?)", height=100)
        example_comment = st.text_area("💬 Exemple de commentaire")
        submit_test = st.form_submit_button("💡 Tester le prompt")

    if submit_test:
        if prompt and example_comment:
            with st.spinner("Appel au modèle..."):
                response = ask_deepseek(prompt, example_comment)
                st.success("Réponse du LLM :")
                st.write(response)
        else:
            st.warning("Merci de remplir le prompt et un exemple de commentaire.")

    # ----------------------
    # 2️⃣ Analyse complète protégée
    # ----------------------
    st.header("📂 2. Analyse d’un fichier complet (accès restreint)")

    password = st.text_input("🔐 Mot de passe requis pour cette section :", type="password")

    if password == PROTECTED_PASSWORD:
        uploaded_file = st.file_uploader("Déposez un fichier Excel contenant une colonne 'Commentaire'", type=["xlsx"])

        if uploaded_file:
            df = pd.read_excel(uploaded_file)

            if 'Commentaire' not in df.columns:
                st.error("Erreur : le fichier doit contenir une colonne nommée 'Commentaire'.")
            else:
                analysis_prompt = st.text_area("✍️ Prompt à appliquer à tous les commentaires", value=prompt or "")
                if st.button("⚙️ Lancer l’analyse"):
                    if not analysis_prompt:
                        st.warning("Merci d'indiquer un prompt.")
                    else:
                        with st.spinner("Analyse rapide en cours..."):
                            MAX_COMMENTS = 1000
                            if len(df) > MAX_COMMENTS:
                                st.warning(f"Le fichier contient plus de {MAX_COMMENTS} commentaires. Seuls {MAX_COMMENTS} seront analysés.")
                                df = df.head(MAX_COMMENTS)

                            loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(loop)
                            results = loop.run_until_complete(process_all_comments(df['Commentaire'], analysis_prompt))

                            df['Réponse_LLM'] = results

                            output = io.BytesIO()
                            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                df.to_excel(writer, index=False, sheet_name='Résultats')

                            st.success("Analyse terminée ✅")
                            st.download_button(
                                label="📥 Télécharger le fichier avec les réponses",
                                data=output,
                                file_name="commentaires_analyse_LLM.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )

    else:
        if password:
            st.error("Mot de passe incorrect.")
