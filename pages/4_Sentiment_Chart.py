import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob
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

# ---------- Sentiment Function ----------
def get_sentiment(feedback):
    if pd.isna(feedback) or feedback.strip() == "":
        return "neutral"
    polarity = TextBlob(feedback).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# ---------- Page Config ----------
st.set_page_config(page_title="Sentiment Analysis", layout="wide")

# ---------- Load Animation ----------
lottie_thinking = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_8xwudw2v.json")

st.title("🧠 Sentiment Analysis of User Feedback")

if "df" not in st.session_state:
    st.warning("Please upload data on the Home page first.")
    st.stop()

df = st.session_state.df

# Filter drop-offs
dropoffs = df[df["completed"] == "no"].copy()

# Show animation near header
if lottie_thinking:
    st_lottie(lottie_thinking, height=100, key="thinking_anim")

# Calculate sentiment
dropoffs["sentiment"] = dropoffs["feedback"].apply(get_sentiment)

sentiment_summary = dropoffs.groupby(["step", "sentiment"]).size().reset_index(name='count')

st.subheader("Sentiment Breakdown Data")
st.dataframe(sentiment_summary)

st.subheader("Sentiment Distribution per Step")
fig_sent = px.bar(
    sentiment_summary,
    x="step",
    y="count",
    color="sentiment",
    barmode="stack",
    title="Sentiment per Onboarding Step",
    color_discrete_map={"positive": "green", "neutral": "gray", "negative": "red"},
    labels={"count": "Feedback Count", "step": "Onboarding Step"}
)
st.plotly_chart(fig_sent, use_container_width=True)

