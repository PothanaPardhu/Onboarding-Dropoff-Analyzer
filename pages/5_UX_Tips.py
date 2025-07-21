import streamlit as st
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
st.set_page_config(page_title="UX Improvement Tips", layout="wide")

# ---------- Load Animation ----------
lottie_idea = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_hudgixqg.json")

st.title("💡 Smart UX Improvement Tips")

if "df" not in st.session_state:
    st.warning("Please upload data on the Home page first.")
    st.stop()

df = st.session_state.df

# Filter drop-offs steps
dropoffs = df[df["completed"] == "no"].copy()
steps = dropoffs["step"].unique()

# Show animation near header
if lottie_idea:
    st_lottie(lottie_idea, height=120, key="idea_anim")

# Static UX tips dictionary
recommendations = {
    "email_verification": "✅ Use reliable OTP provider & allow resending OTP.",
    "profile_setup": "✅ Reduce form fields, make photo upload smoother.",
    "feature_tour": "✅ Add 'Skip Tour' button & keep the tour concise.",
    "first_action": "✅ Provide a clear CTA like 'Start here' with onboarding tooltip.",
    "upgrade_prompt": "✅ Show value of upgrade before prompting payment."
}

for step in steps:
    tip = recommendations.get(step, "Consider simplifying or explaining this step better.")
    st.markdown(f"🔹 **{step}**: {tip}")
