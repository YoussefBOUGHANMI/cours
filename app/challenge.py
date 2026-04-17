import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURATION ---
COST_CONTACT = 800
GAIN_PER_SALE = 5000
MAX_SUBMISSIONS = 10
TEAMS = ["Equipe 1", "Equipe 2" ,"Equipe 3" , "Equipe 4" , "Equipe 5" ]
PASSWORD = "admin13081996"  # 🔐 à modifier par toi-même

TARGET_PATH = "/mount/src/cours/app/data_test_target.csv"
LEADERBOARD_PATH = "/mount/src/cours/app/leaderboard.csv"

# --- FONCTIONS ---
def eval_strategy(submitted_ids, target_df):
    matched = target_df[target_df["Id"].isin(submitted_ids)]
    num_contacted = len(submitted_ids)
    num_subscribed = matched["Response"].sum()
    benefit = (num_subscribed * GAIN_PER_SALE) - (num_contacted * COST_CONTACT)
    return num_contacted, int(num_subscribed), int(benefit)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_PATH):
        return pd.read_csv(LEADERBOARD_PATH)
    else:
        return pd.DataFrame(columns=["Team", "Date", "Nb contactés", "Nb souscriptions", "Bénéfice (€)", "Tentatives restantes"])

def save_to_leaderboard(team, num_contacted, num_subscribed, benefit, tries_left):
    leaderboard = load_leaderboard()
    new_entry = {
        "Team": team,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Nb contactés": num_contacted,
        "Nb souscriptions": num_subscribed,
        "Bénéfice (€)": benefit,
        "Tentatives restantes": tries_left
    }
    leaderboard = pd.concat([leaderboard, pd.DataFrame([new_entry])], ignore_index=True)
    leaderboard.to_csv(LEADERBOARD_PATH, index=False)

def get_team_submission_count(leaderboard, team):
    return leaderboard[leaderboard["Team"] == team].shape[0]

# --- INTERFACE ---
def Challenge() :
    
    st.title("🏆 Challenge Machine Learning - GéniaLum")

    st.markdown("""
    Bienvenue dans le challenge **GéniaLum** !

    **Objectif** : Sélectionner les clients à contacter pour maximiser le bénéfice.

    - 💸 Coût de démarchage : **800 €** par client
    - 🤑 Gain par vente : **5 000 €**

    """)
    [st.write("\n") for i in range(2)]
    
    col1,col2,col3 = st.columns(3)
    
    [st.write("\n") for i in range(2)]
    
    st.markdown("Chaque équipe a droit à **3 tentatives maximum**.")
    
    # Encadré pour cette section
    with col2:


        with open("/mount/src/cours/app/data_train.csv", "rb") as file_tp1:
            st.download_button(
                label="Télecharger les données historique",
                data=file_tp1,
                file_name="data_historique.csv",
                mime="text/csv",
            )
        
        
    # Encadré pour cette section
    with col3:
        with open("/mount/src/cours/app/data_test.csv", "rb") as file_tp1:
            st.download_button(
                label="Télecharger les données des clients à contacter",
                data=file_tp1,
                file_name="clients_a_contacter.csv",
                mime="text/csv",
            )
        
        
    with col1:
        
        with open("/mount/src/cours/app/🎯 Consignes du Challenge Machine Learning.docx", "rb") as file:
            st.download_button(
            label="Télécharger les Consignes du Challenge",
            data=file,
            file_name="Consignes.docx",
        )
        
        
        
        
        
        
        
        
        
        
        

    # --- FORMULAIRE DE SOUMISSION ---
    with st.form("Soumission"):
        team = st.selectbox("Sélectionnez votre équipe :", TEAMS)
        password = st.text_input("Mot de passe (organisateur)", type="password")
        uploaded_file = st.file_uploader("Déposez votre fichier Excel (.xlsx) avec une colonne 'ID'", type=["xlsx"])
        submit_button = st.form_submit_button("Valider la stratégie")

    if submit_button:
        leaderboard = load_leaderboard()
        submission_count = get_team_submission_count(leaderboard, team)

        if password != PASSWORD:
            st.error("Mot de passe incorrect.")
        elif submission_count >= MAX_SUBMISSIONS:
            st.warning(f"⛔ L'équipe **{team}** a déjà utilisé ses {MAX_SUBMISSIONS} tentatives.")
        elif uploaded_file is None:
            st.error("Veuillez déposer un fichier CSV contenant une colonne 'Id'.")
        else:
            try:
                df_submission = pd.read_excel(uploaded_file)
                if "Id" not in df_submission.columns:
                    st.error("Le fichier doit contenir une colonne nommée 'Id'.")
                else:
                    submitted_ids = df_submission["Id"].dropna().astype(int).unique()
                    df_target = pd.read_csv(TARGET_PATH)

                    num_contacted, num_subscribed, benefit = eval_strategy(submitted_ids, df_target)
                    tries_left = MAX_SUBMISSIONS - (submission_count + 1)

                    st.success(f"📬 Clients contactés : {num_contacted}")
                    st.success(f"✅ Souscriptions confirmées : {num_subscribed}")
                    st.info(f"💰 Bénéfice net : {benefit:,} €")
                    st.info(f"🔁 Tentatives restantes pour {team} : {tries_left}")

                    save_to_leaderboard(team, num_contacted, num_subscribed, benefit, tries_left)

            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")

    # --- LEADERBOARD ---
    st.markdown("---")
    st.subheader("📊 Classement des équipes")

    leaderboard = load_leaderboard()

    if leaderboard.empty:
        st.info("Aucune soumission pour le moment.")
    else:
        # Récupère la meilleure soumission par équipe (max bénéfice)
        best_per_team = leaderboard.sort_values("Bénéfice (€)", ascending=False).drop_duplicates("Team", keep="first")

        # Recalcul des tentatives restantes à partir de toutes les soumissions
        team_submission_counts = leaderboard["Team"].value_counts().to_dict()
        best_per_team["Tentatives restantes"] = best_per_team["Team"].str.replace(" 👑", "").map(
            lambda t: MAX_SUBMISSIONS - team_submission_counts.get(t, 0)
        )

        # Ajouter une couronne à la meilleure équipe
        best_per_team = best_per_team.sort_values("Bénéfice (€)", ascending=False).reset_index(drop=True)
        if not best_per_team.empty:
            best_per_team.loc[0, "Team"] += " 👑"

        st.dataframe(
            best_per_team[["Team", "Nb contactés", "Nb souscriptions", "Bénéfice (€)", "Tentatives restantes"]]
            .style.highlight_max(axis=0),
            use_container_width=True
        )


