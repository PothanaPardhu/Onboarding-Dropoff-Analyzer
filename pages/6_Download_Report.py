import streamlit as st
import pandas as pd
from io import StringIO, BytesIO
from streamlit_lottie import st_lottie
import requests

# ---------- Custom Styling ----------
st.markdown("""
    <style>
        /* Neon effect for title */
        .main h1 {
            font-size: 3em;
            color: #39ff14;
            text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14;
        }

        /* Sidebar with glowing border and hover effects */
        section[data-testid="stSidebar"] {
            background-color: #0f0f0f;
            border-right: 4px solid #00ffff;
            box-shadow: 0 0 20px #00ffff;
        }

        section[data-testid="stSidebar"] a {
            color: #39ff14;
            padding: 10px;
            display: block;
            border-radius: 8px;
            margin-bottom: 5px;
            transition: all 0.3s ease;
            background: linear-gradient(to right, #111, #1a1a1a);
            box-shadow: 0 0 10px #39ff14;
        }

        section[data-testid="stSidebar"] a:hover {
            background-color: #00ffff;
            color: #0f0f0f !important;
            font-weight: bold;
            box-shadow: 0 0 20px #00ffff;
            transform: scale(1.05);
        }

        /* Neon styled file uploader */
        .stFileUploader label div {
            border: 2px dashed #ff00ff;
            background-color: #1a1a1a;
            padding: 12px;
            border-radius: 10px;
            color: #ffffff;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 10px #ff00ff;
        }

        .stFileUploader label div:hover {
            border-color: #00ffff;
            background-color: #222;
            box-shadow: 0 0 20px #00ffff;
        }

        /* Glowing DataFrame border */
        .stDataFrame {
            border: 2px solid #39ff14;
            border-radius: 10px;
            box-shadow: 0 0 10px #39ff14;
        }

        /* Divider glow effect */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, #ff00ff, #00ffff);
            box-shadow: 0 0 20px #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Utility: Load Lottie Animation ----------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- Page Config ----------
# st.set_page_config(page_title="Download Report", layout="wide")

# ---------- Load Animation ----------
lottie_download = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_totrpclr.json")
lottie_success = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json")

st.title("📥 Download Your Onboarding Analysis Report")

if "df" not in st.session_state:
    st.warning("Please upload data on the Home page first.")
    st.stop()

df = st.session_state.df

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(df)

if lottie_download:
    st_lottie(lottie_download, height=150, key="download_anim")

st.markdown("Download the full onboarding data you uploaded for your records.")

st.download_button(
    label="Download CSV Report",
    data=csv_data,
    file_name="onboarding_data_report.csv",
    mime="text/csv"
)