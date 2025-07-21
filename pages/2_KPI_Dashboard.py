import streamlit as st
import pandas as pd
import plotly.express as px
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

# Load Lottie animation helper
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_kpi_header = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_vf7yw3cn.json")  # example KPI animation
lottie_success = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json")  # success animation

st.set_page_config(page_title="KPI Dashboard", layout="wide", page_icon="📊")

st.title("📈 KPI Dashboard")

if "df" in st.session_state:
    df = st.session_state.df

    # Calculations
    total_users = len(df)
    completed_users = df[df["completed"] == "yes"].shape[0]
    dropoff_users = df[df["completed"] == "no"].shape[0]
    dropoff_rate = (dropoff_users / total_users) * 100 if total_users else 0

    # Average completion time (if 'time_spent' column exists)
    avg_time = None
    if "time_spent" in df.columns:
        avg_time = df[df["completed"] == "yes"]["time_spent"].mean()

    # Header animation
    if lottie_kpi_header:
        st_lottie(lottie_kpi_header, height=150, key="kpi_header")

    # Display KPIs
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    kpi_col1.metric("Total Users Started", total_users)
    kpi_col2.metric("Users Completed", completed_users)
    kpi_col3.metric("Drop-off Count", dropoff_users)
    kpi_col4.metric("Drop-off Rate (%)", f"{dropoff_rate:.2f}")

    if avg_time is not None:
        st.metric("Average Completion Time (mins)", f"{avg_time:.2f}")

    # Funnel Chart for drop-offs
    step_counts = df.groupby("step")["completed"].apply(lambda x: (x=="yes").sum()).reset_index()
    step_counts.columns = ["Step", "Users Completed Step"]

    fig = px.bar(step_counts, x="Step", y="Users Completed Step",
                 title="Users Completing Each Step",
                 labels={"Users Completed Step": "Users Completed", "Step": "Onboarding Step"},
                 color="Users Completed Step", color_continuous_scale="Blues")

    st.plotly_chart(fig, use_container_width=True)

    # Celebration animation at the end
    if lottie_success:
        st_lottie(lottie_success, height=180, key="success_kpi")

else:
    st.warning("⚠️ Please upload the onboarding CSV file first on the Home page.")
