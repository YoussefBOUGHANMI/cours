import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
import re
import io
from googleapiclient.errors import HttpError

def get_video_id(youtube_url):
    """Extrait l'ID de la vidéo à partir d'un lien YouTube."""
    regex = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, youtube_url)
    return match.group(1) if match else None

def get_all_comments(video_id, api_key):
    """Récupère tous les commentaires possibles tant que l'API répond."""
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    next_page_token = None
    total = 0

    while True:
        try:
            request = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=next_page_token,
                maxResults=100,
                textFormat='plainText'
            )
            response = request.execute()

            for item in response.get('items', []):
                snippet = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    "Auteur": snippet['authorDisplayName'],
                    "Commentaire": snippet['textDisplay'],
                    "Publié le": snippet['publishedAt']
                })

            total += len(response.get('items', []))
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        except HttpError as e:
            st.error(f"Erreur API : {e}")
            break
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
            break

    return pd.DataFrame(comments)


def display_comment():
    # === Streamlit UI ===
    st.title("📺 YouTube Comment Extractor")
    
    
    [st.write("\n") for i in range(2)]
    st.write("----")
    [st.write("\n") for i in range(2)]
    
    st.markdown(
    """
    ⚠️ Pour utiliser cette interface, vous devez **créer un compte Google** (si vous n'en avez pas déjà un) et **générer une clé API** via la Google Cloud Console.  
    Vous pouvez le faire en vous rendant sur ce lien : [https://console.developers.google.com/](https://console.developers.google.com/)
    """
)
    
    [st.write("\n") for i in range(2)]
    st.write("----")
    [st.write("\n") for i in range(2)]

    api_key = st.text_input("🔑 Entrez votre clé API YouTube", type="password")
    video_url = st.text_input("📎 Collez le lien de la vidéo YouTube")

    if st.button("📥 Récupérer TOUS les commentaires"):
        if not api_key or not video_url:
            st.warning("Merci d'entrer une clé API et une URL valides.")
        else:
            with st.spinner("Récupération de tous les commentaires..."):
                video_id = get_video_id(video_url)
                if video_id:
                    df = get_all_comments(video_id, api_key)
                    if not df.empty:
                        st.success(f"{len(df)} commentaires récupérés !")
                        buffer = io.BytesIO()
                        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                            df.to_excel(writer, index=False, sheet_name='Commentaires')
                        st.download_button(
                            label="📄 Télécharger les commentaires (Excel)",
                            data=buffer,
                            file_name='youtube_comments_complets.xlsx',
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                    else:
                        st.info("Aucun commentaire trouvé ou quota épuisé.")
                else:
                    st.error("Lien de vidéo invalide.")
