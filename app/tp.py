import streamlit as st




def TP():



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



    for i in range(5):
        st.write("\n")


    texte = """<div width="704" style="text-align: start;color: rgb(0, 0, 0);">
        <div>
            <div style='font-family: "'>
                <div style="color: rgb(75, 0, 130);font-size: 1.5em;"><span style="color: rgb(0, 0, 0);"><strong>TP1 : Score d&rsquo;app&eacute;tence bancaire&nbsp;</strong></span>
                    <div><br></div>
                </div>
            </div>
        </div>
    </div>
    <div style="text-align: start;color: rgb(0, 0, 0);">
        <div style='text-align: start;color: rgb(49, 51, 63);font-size: 16px;font-family: "'>
            <div width="704">
                <div width="704"></div>
            </div>
        </div>
    </div>
    <p style="margin: 0cm 0cm 8pt;line-height: 18.4px;font-size: medium;font-family: Calibri, sans-serif;color: rgb(0, 0, 0);font-style: normal;font-weight: 400;text-align: start;text-indent: 0px;text-decoration: none;">Les donn&eacute;es concernent les campagnes de marketing direct (appels t&eacute;l&eacute;phoniques) d&apos;une institution bancaire portugaise. L&apos;objectif de la classification est de pr&eacute;dire si le client souscrira un d&eacute;p&ocirc;t &agrave; terme (variable y).</p>
    """





    texte2 = """
    <div width="704" style="text-align: start;color: rgb(0, 0, 0);">
        <div>
            <div style='font-family: "'>
                <p style="margin: 0cm 0cm 8pt;line-height: 18.4px;font-size: medium;font-family: Calibri, sans-serif;color: rgb(0, 0, 0);font-style: normal;font-weight: 400;text-align: start;text-indent: 0px;text-decoration: none;"><span style="font-size: 20px;"><em><strong>La description des donn&eacute;es est la suivante :&nbsp;</strong></em></span></p>
                <p style="margin: 0cm 0cm 8pt;line-height: 18.4px;font-size: medium;font-family: Calibri, sans-serif;color: rgb(0, 0, 0);font-style: normal;font-weight: 400;text-align: start;text-indent: 0px;text-decoration: none;"><br></p>
                <ul>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">age</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">job : type of job</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">marital : marital status&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">education&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">default</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">balance</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">housing: has housing loan?&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">loan: has personal loan?</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">contact</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">day: last contact day of the month&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">month: last contact month of year&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">duration: last contact duration, in seconds&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">campaign: number of contacts performed during this campaign and for this client&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">pdays: number of days that passed by after the client was last contacted from a previous campaign&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">previous: number of contacts performed before this campaign and for this client&nbsp;</li>
                    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; line-height: 18.4px; font-size: medium; font-family: Calibri, sans-serif; color: rgb(0, 0, 0); font-style: normal; font-weight: 400; text-align: start; text-indent: 0px; text-decoration: none;">poutcome: outcome of the previous marketing campaign </li>
                </ul>
            </div>
        </div>
    </div>
    """








    st.markdown('<div class="section-box">' + texte + '</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box">' + texte2 + '</div>', unsafe_allow_html=True)





    # Encadré pour cette section
    with st.container():



        # Fichier pour le TP1
        with open("/mount/src/cours/app/bank.csv", "rb") as file_tp1:
            st.download_button(
                label="Télecharger le jeu de données",
                data=file_tp1,
                file_name="TP1.csv",
                mime="text/csv",
                key="tp1_download",  # key nécessaire si plusieurs boutons
                help="Cliquez pour télécharger le fichier TP1"
            )
        st.markdown('</div>', unsafe_allow_html=True)





    
