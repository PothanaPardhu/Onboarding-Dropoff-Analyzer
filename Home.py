# # ---------- Home.py ----------
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from streamlit_lottie import st_lottie
# import requests

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- App Config ----------
# st.set_page_config(page_title="Onboarding Drop-off Analyzer",
#                    layout="wide",
#                    page_icon="📊")

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")

# # ---------- Header Section ----------
# col1, col2 = st.columns([2, 3])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=200)

# with col2:
#     st.title("📉 Onboarding Drop-off Analyzer")
#     st.markdown("""
#     Welcome to the **AI-Powered Onboarding Analyzer** 🚀

#     Upload your onboarding journey data, identify where users drop off,
#     and visualize it in a simple dashboard — all in one place.
#     """)

# # ---------- Divider & Animation ----------
# st.divider()
# if lottie_header:
#     st_lottie(lottie_header, height=180)

# # ---------- File Upload ----------
# uploaded_file = st.file_uploader("📥 Upload your onboarding CSV file", type="csv")

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.session_state.df = df  # Save to session for use in other pages
#     st.subheader("📄 Preview of Uploaded Data")
#     st.dataframe(df.head())
  
# else:
#     st.info("👆 Upload a CSV file to get started!")














#GOOD BUT NOT SUPERB


# # ---------- Home.py ----------
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from streamlit_lottie import st_lottie
# import requests

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- Custom Styling ----------
# st.markdown("""
#     <style>
#         /* Neon effect for title */
#         .main h1 {
#             font-size: 3em;
#             color: #39ff14;
#             text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14;
#         }

#         /* Sidebar with glowing border */
#         section[data-testid="stSidebar"] {
#             background-color: #0f0f0f;
#             border-right: 4px solid #00ffff;
#             box-shadow: 0 0 10px #00ffff;
#         }

#         /* Hover effect for sidebar links */
#         section[data-testid="stSidebar"] a:hover {
#             color: #ff00ff !important;
#             font-weight: bold;
#             transform: scale(1.05);
#             transition: all 0.3s ease-in-out;
#         }

#         /* Neon styled file uploader */
#         .stFileUploader label div {
#             border: 2px dashed #ff00ff;
#             background-color: #1a1a1a;
#             padding: 12px;
#             border-radius: 10px;
#             color: #ffffff;
#             transition: all 0.3s ease-in-out;
#             box-shadow: 0 0 10px #ff00ff;
#         }

#         .stFileUploader label div:hover {
#             border-color: #00ffff;
#             background-color: #222;
#             box-shadow: 0 0 20px #00ffff;
#         }

#         /* Glowing DataFrame border */
#         .stDataFrame {
#             border: 2px solid #39ff14;
#             border-radius: 10px;
#             box-shadow: 0 0 10px #39ff14;
#         }

#         /* Divider glow effect */
#         hr {
#             border: none;
#             height: 2px;
#             background: linear-gradient(to right, #ff00ff, #00ffff);
#             box-shadow: 0 0 20px #00ffff;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # ---------- App Config ----------
# st.set_page_config(page_title="Onboarding Drop-off Analyzer",
#                    layout="wide",
#                    page_icon="📊")

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")

# # ---------- Header Section ----------
# col1, col2 = st.columns([2, 3])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=200)

# with col2:
#     st.title("📉 Onboarding Drop-off Analyzer")
#     st.markdown("""
#     <span style='color:#00ffff;font-size:18px;'>Welcome to the <strong>AI-Powered Onboarding Analyzer</strong> 🚀</span><br><br>
#     Upload your onboarding journey data, identify where users drop off,
#     and visualize it in a beautiful dashboard — all in one place.
#     """, unsafe_allow_html=True)

# # ---------- Divider & Animation ----------
# st.divider()
# if lottie_header:
#     st_lottie(lottie_header, height=180)

# # ---------- File Upload ----------
# uploaded_file = st.file_uploader("📥 Upload your onboarding CSV file", type="csv")

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.session_state.df = df  # Save to session for use in other pages
#     st.subheader("📄 Preview of Uploaded Data")
#     st.dataframe(df.head())
# else:
#     st.info("👆 Upload a CSV file to get started!")






#COOLEST ONE


# # ---------- Home.py ----------
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from streamlit_lottie import st_lottie
# import requests

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- Custom Styling ----------
# st.markdown("""
#     <style>
#         /* Neon effect for title */
#         .main h1 {
#             font-size: 3em;
#             color: #39ff14;
#             text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14;
#         }

#         /* Sidebar with glowing border and hover effects */
#         section[data-testid="stSidebar"] {
#             background-color: #0f0f0f;
#             border-right: 4px solid #00ffff;
#             box-shadow: 0 0 20px #00ffff;
#         }

#         section[data-testid="stSidebar"] a {
#             color: #39ff14;
#             padding: 10px;
#             display: block;
#             border-radius: 8px;
#             margin-bottom: 5px;
#             transition: all 0.3s ease;
#             background: linear-gradient(to right, #111, #1a1a1a);
#             box-shadow: 0 0 10px #39ff14;
#         }

#         section[data-testid="stSidebar"] a:hover {
#             background-color: #00ffff;
#             color: #0f0f0f !important;
#             font-weight: bold;
#             box-shadow: 0 0 20px #00ffff;
#             transform: scale(1.05);
#         }

#         /* Neon styled file uploader */
#         .stFileUploader label div {
#             border: 2px dashed #ff00ff;
#             background-color: #1a1a1a;
#             padding: 12px;
#             border-radius: 10px;
#             color: #ffffff;
#             transition: all 0.3s ease-in-out;
#             box-shadow: 0 0 10px #ff00ff;
#         }

#         .stFileUploader label div:hover {
#             border-color: #00ffff;
#             background-color: #222;
#             box-shadow: 0 0 20px #00ffff;
#         }

#         /* Glowing DataFrame border */
#         .stDataFrame {
#             border: 2px solid #39ff14;
#             border-radius: 10px;
#             box-shadow: 0 0 10px #39ff14;
#         }

#         /* Divider glow effect */
#         hr {
#             border: none;
#             height: 2px;
#             background: linear-gradient(to right, #ff00ff, #00ffff);
#             box-shadow: 0 0 20px #00ffff;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # ---------- App Config ----------
# st.set_page_config(page_title="Onboarding Drop-off Analyzer",
#                    layout="wide",
#                    page_icon="📊")

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")

# # ---------- Header Section ----------
# col1, col2 = st.columns([2, 3])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=200)

# with col2:
#     st.title("📉 Onboarding Drop-off Analyzer")
#     st.markdown("""
#     <span style='color:#00ffff;font-size:18px;'>Welcome to the <strong>AI-Powered Onboarding Analyzer</strong> 🚀</span><br><br>
#     Upload your onboarding journey data, identify where users drop off,
#     and visualize it in a beautiful dashboard — all in one place.
#     """, unsafe_allow_html=True)

# # ---------- Divider & Animation ----------
# st.divider()
# if lottie_header:
#     st_lottie(lottie_header, height=180)

# # ---------- File Upload ----------
# uploaded_file = st.file_uploader("📥 Upload your onboarding CSV file", type="csv")

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.session_state.df = df  # Save to session for use in other pages
#     st.subheader("📄 Preview of Uploaded Data")
#     st.dataframe(df.head())
# else:
#     st.info("👆 Upload a CSV file to get started!")





# # ---------- Home.py ----------
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from streamlit_lottie import st_lottie
# import requests

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- Custom Styling ----------
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
#             color: white;
#             font-family: 'Segoe UI', sans-serif;
#         }

#         /* Neon effect for title */
#         .main h1 {
#             font-size: 3em;
#             color: #39ff14;
#             text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14;
#         }

#         /* Sidebar with glowing border and hover effects */
#         section[data-testid="stSidebar"] {
#             background-color: #0f0f0f;
#             border-right: 4px solid #00ffff;
#             box-shadow: 0 0 20px #00ffff;
#         }

#         section[data-testid="stSidebar"] a {
#             color: #39ff14;
#             padding: 10px;
#             display: block;
#             border-radius: 8px;
#             margin-bottom: 5px;
#             transition: all 0.3s ease;
#             background: linear-gradient(to right, #111, #1a1a1a);
#             box-shadow: 0 0 10px #39ff14;
#             font-weight: bold;
#         }

#         section[data-testid="stSidebar"] a:hover {
#             background-color: #00ffff;
#             color: #0f0f0f !important;
#             font-weight: bold;
#             box-shadow: 0 0 20px #00ffff;
#             transform: scale(1.05);
#         }

#         /* Neon styled file uploader */
#         .stFileUploader label div {
#             border: 2px dashed #ff00ff;
#             background-color: #1a1a1a;
#             padding: 12px;
#             border-radius: 10px;
#             color: #ffffff;
#             transition: all 0.3s ease-in-out;
#             box-shadow: 0 0 10px #ff00ff;
#         }

#         .stFileUploader label div:hover {
#             border-color: #00ffff;
#             background-color: #222;
#             box-shadow: 0 0 20px #00ffff;
#         }

#         /* Glowing DataFrame border */
#         .stDataFrame {
#             border: 2px solid #39ff14;
#             border-radius: 10px;
#             box-shadow: 0 0 10px #39ff14;
#         }

#         /* Divider glow effect */
#         hr {
#             border: none;
#             height: 2px;
#             background: linear-gradient(to right, #ff00ff, #00ffff);
#             box-shadow: 0 0 20px #00ffff;
#         }

#         /* Button Hover Animation */
#         button[kind="primary"] {
#             background-color: #00ffff !important;
#             color: #0f0f0f;
#             font-weight: bold;
#             border-radius: 8px;
#             border: none;
#             box-shadow: 0 0 10px #00ffff;
#             transition: 0.3s ease-in-out;
#         }

#         button[kind="primary"]:hover {
#             background-color: #ff00ff !important;
#             color: white;
#             transform: scale(1.1);
#             box-shadow: 0 0 20px #ff00ff;
#         }

#         /* Markdown text styling */
#         .main p, .main span, .main li {
#             font-size: 1.1em;
#             line-height: 1.6;
#             color: #ffffff;
#             text-shadow: 0 0 2px #00ffff;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # ---------- App Config ----------
# st.set_page_config(page_title="Onboarding Drop-off Analyzer",
#                    layout="wide",
#                    page_icon="📊")

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")

# # ---------- Header Section ----------
# col1, col2 = st.columns([2, 3])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=200)

# with col2:
#     st.title("📉 Onboarding Drop-off Analyzer")
#     st.markdown("""
#     <span style='color:#00ffff;font-size:18px;'>Welcome to the <strong>AI-Powered Onboarding Analyzer</strong> 🚀</span><br><br>
#     Upload your onboarding journey data, identify where users drop off,
#     and visualize it in a beautiful dashboard — all in one place.
#     """, unsafe_allow_html=True)

# # ---------- Divider & Animation ----------
# st.divider()
# if lottie_header:
#     st_lottie(lottie_header, height=180)

# # ---------- File Upload ----------
# uploaded_file = st.file_uploader("📥 Upload your onboarding CSV file", type="csv")

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.session_state.df = df  # Save to session for use in other pages
#     st.subheader("📄 Preview of Uploaded Data")
#     st.dataframe(df.head())
# else:
#     st.info("👆 Upload a CSV file to get started!")












#ERROR OCCURED 



# # ---------- Home.py ----------
# import streamlit as st
# import pandas as pd
# from streamlit_lottie import st_lottie
# import requests
# from streamlit.components.v1 import html

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- Custom Styling ----------
# st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Roboto+Mono&family=Montserrat:wght@900&display=swap');
        
#         /* Main background */
#         body {
#             background: linear-gradient(135deg, #0f0524 0%, #1a0933 100%);
#             color: #ffffff;
#             font-family: 'Roboto Mono', monospace;
#         }
        
#         /* Title animation */
#         @keyframes neonPulse {
#             0% { text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff; }
#             50% { text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff5e00, 0 0 40px #ff00ff; }
#             100% { text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff; }
#         }
        
#         @keyframes orangePulse {
#             0% { text-shadow: 0 0 5px #ff5e00; }
#             50% { text-shadow: 0 0 20px #ff5e00, 0 0 30px #ff5e00; }
#             100% { text-shadow: 0 0 5px #ff5e00; }
#         }
        
#         .main h1 {
#             font-family: 'Orbitron', sans-serif;
#             font-size: 2.8rem;
#             color: #ff00ff;
#             animation: neonPulse 2s infinite;
#             text-align: center;
#             margin-bottom: 1rem;
#             letter-spacing: 2px;
#         }
        
#         /* Amazing sidebar */
#         section[data-testid="stSidebar"] {
#             background: rgba(15, 5, 36, 0.85) !important;
#             backdrop-filter: blur(10px);
#             border-right: 2px solid #ff00ff;
#             box-shadow: 0 0 25px rgba(255, 0, 255, 0.5);
#         }
        
#         section[data-testid="stSidebar"] h1 {
#             font-family: 'Montserrat', sans-serif;
#             color: #00ffff;
#             text-shadow: 0 0 10px #00ffff;
#             font-size: 1.8rem;
#             border-bottom: 2px solid #ff5e00;
#             padding-bottom: 10px;
#         }
        
#         section[data-testid="stSidebar"] .css-1d391kg a {
#             font-family: 'Orbitron', sans-serif;
#             color: #ff5e00 !important;
#             font-size: 1rem;
#             margin: 10px 0;
#             padding: 10px 15px;
#             border-radius: 8px;
#             transition: all 0.3s ease;
#             background: rgba(255, 94, 0, 0.1);
#             border-left: 3px solid #ff5e00;
#         }
        
#         section[data-testid="stSidebar"] .css-1d391kg a:hover {
#             background: rgba(255, 94, 0, 0.3) !important;
#             color: #ffffff !important;
#             transform: translateX(5px);
#         }
        
#         /* File uploader styling */
#         .stFileUploader label {
#             font-family: 'Orbitron', sans-serif;
#             color: #00ffff !important;
#             text-shadow: 0 0 5px #00ffff;
#         }
        
#         .stFileUploader label div {
#             background: rgba(0, 0, 0, 0.2) !important;
#             border: 2px dashed #ff5e00 !important;
#             border-radius: 10px !important;
#             padding: 20px !important;
#             transition: all 0.3s ease !important;
#         }
        
#         .stFileUploader label div:hover {
#             border-color: #00ffff !important;
#             box-shadow: 0 0 15px #00ffff !important;
#         }
        
#         /* Content text */
#         .main p {
#             color: #ffffff;
#             font-size: 1.1rem;
#             line-height: 1.6;
#         }
        
#         .main p span.neon-orange {
#             color: #ff5e00;
#             animation: orangePulse 2s infinite;
#             font-weight: bold;
#         }
        
#         .main p span.neon-violet {
#             color: #ff00ff;
#             text-shadow: 0 0 5px #ff00ff;
#             font-weight: bold;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # ---------- App Config ----------
# st.set_page_config(
#     page_title="Onboarding Drop-off Analyzer",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")

# # ---------- Sidebar ----------
# with st.sidebar:
#     st.title("NAVIGATION")
#     st.markdown("[Dashboard](#)", disabled=True)
#     st.markdown("[Analysis](#)", disabled=True)
#     st.markdown("[Visualizations](#)", disabled=True)
    
#     st.markdown("---")
#     st.title("SETTINGS")
#     dark_mode = st.toggle("Dark Mode", value=True)
#     theme_color = st.selectbox("Theme Color", ["Neon Orange", "Cyber Violet", "Electric Blue"])

# # ---------- Main Content ----------
# col1, col2 = st.columns([1, 2])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=250)

# with col2:
#     st.markdown("""
#     <h1>ONBOARDING DROP-OFF ANALYZER</h1>
#     <p>
#         Analyze user journey with our <span class="neon-orange">AI-powered</span> platform that 
#         identifies <span class="neon-violet">drop-off points</span> in your onboarding flow.
#     </p>
#     """, unsafe_allow_html=True)

# # ---------- File Upload Section ----------
# st.markdown("---")
# uploaded_file = st.file_uploader(
#     "UPLOAD YOUR ONBOARDING CSV FILE",
#     type="csv",
#     help="Upload your user onboarding data in CSV format"
# )

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.session_state.df = df
#     st.success("Data uploaded successfully! Here's a preview:")
#     st.dataframe(df.head().style.set_properties(**{
#         'background-color': 'rgba(30, 10, 60, 0.5)',
#         'color': 'white',
#         'border': '1px solid #ff5e00'
#     }))
# else:
#     st.info("Please upload a CSV file to begin analysis")





















# one of the best 




# ---------- Home.py ----------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

# ---------- Utility: Load Lottie Animation ----------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- Custom Styling ----------

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Roboto+Mono&display=swap');

        /* Global font and background */
        body {
            background: linear-gradient(to right, #000428, #004e92);
            color: #ffffff;
            font-family: 'Roboto Mono', monospace;
        }

        /* Title neon style */
        .main h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.2em;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #39ff14;
        }

        /* Sidebar background and glow */
        section[data-testid="stSidebar"] {
            background: #0e0e0e;
            box-shadow: 0 0 15px #00ffff;
            border-right: 3px solid #00ffff;
        }

        /* Sidebar text and hover */
        section[data-testid="stSidebar"] .css-1d391kg a {
            font-family: 'Orbitron', sans-serif;
            color: #ff00ff;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 16px;
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 8px;
            transition: 0.4s ease-in-out;
            box-shadow: 0 0 10px #ff00ff;
            background: rgba(255, 255, 255, 0.05);
        }

        section[data-testid="stSidebar"] .css-1d391kg a:hover {
            background-color: #00ffff;
            color: black !important;
            box-shadow: 0 0 20px #00ffff;
            transform: scale(1.05);
        }

        /* Sidebar title text */
        section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
            color: #39ff14;
            text-shadow: 0 0 10px #39ff14;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }

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
            font-weight: bold;
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

        /* Button Hover Animation */
        button[kind="primary"] {
            background-color: #00ffff !important;
            color: #0f0f0f;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            box-shadow: 0 0 10px #00ffff;
            transition: 0.3s ease-in-out;
        }

        button[kind="primary"]:hover {
            background-color: #ff00ff !important;
            color: white;
            transform: scale(1.1);
            box-shadow: 0 0 20px #ff00ff;
        }

        /* Markdown text styling */
        .main p, .main span, .main li {
            font-size: 1.1em;
            line-height: 1.6;
            color: #ffffff;
            text-shadow: 0 0 2px #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- App Config ----------
st.set_page_config(page_title="Onboarding Drop-off Analyzer",
                   layout="wide",
                   page_icon="📊")

# ---------- Load Animations ----------
lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")

# ---------- Header Section ----------
col1, col2 = st.columns([2, 3])

with col1:
    if lottie_analytics:
        st_lottie(lottie_analytics, height=200)

with col2:
    st.title("📉 Onboarding Drop-off Analyzer")
    st.markdown("""
    <span style='color:#00ffff;font-size:18px;'>Welcome to the <strong>AI-Powered Onboarding Analyzer</strong> 🚀</span><br><br>
    Upload your onboarding journey data, identify where users drop off,
    and visualize it in a beautiful dashboard — all in one place.
    """, unsafe_allow_html=True)

# ---------- Divider & Animation ----------
st.divider()
if lottie_header:
    st_lottie(lottie_header, height=180)

# ---------- File Upload ----------
uploaded_file = st.file_uploader("📥 Upload your onboarding CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df  # Save to session for use in other pages
    st.subheader("📄 Preview of Uploaded Data")
    st.dataframe(df.head())
else:
    st.info("👆 Upload a CSV file to get started!")














#one of the not bad 

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from streamlit_lottie import st_lottie
# import requests
# import time
# from typing import Optional

# # ---------- Utility: Load Lottie Animation ----------
# def load_lottie_url(url: str) -> Optional[dict]:
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ---------- Custom Styling with Advanced Animations ----------
# st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Poppins:wght@300;400;600;700&family=Montserrat:wght@900&family=Audiowide&display=swap');
        
#         /* Cosmic Background with Stars */
#         body {
#             background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
#             color: #ffffff;
#             font-family: 'Poppins', sans-serif;
#             overflow-x: hidden;
#         }
        
#         /* Starfield Animation */
#         @keyframes animStar {
#             from { transform: translateY(0px); }
#             to { transform: translateY(-2000px); }
#         }
        
#         /* Add star elements */
#         .stars {
#             position: fixed;
#             top: 0;
#             left: 0;
#             right: 0;
#             bottom: 0;
#             width: 100%;
#             height: 100%;
#             display: block;
#             z-index: -1;
#         }
        
#         .stars:after {
#             content: "";
#             position: absolute;
#             top: 2000px;
#             width: 1px;
#             height: 1px;
#             background: transparent;
#             box-shadow: 892px 1232px #fff, 125px 1096px #fff, 1024px 1081px #fff, 
#                          417px 1227px #fff, 983px 715px #fff, 1158px 1165px #fff, 
#                          668px 293px #fff, 1266px 199px #fff, 382px 493px #fff, 
#                          117px 484px #fff;
#             animation: animStar 50s linear infinite;
#         }
        
#         .stars:before {
#             content: "";
#             position: absolute;
#             top: 2000px;
#             width: 2px;
#             height: 2px;
#             background: transparent;
#             box-shadow: 892px 1232px #fff, 125px 1096px #fff, 1024px 1081px #fff, 
#                          417px 1227px #fff, 983px 715px #fff, 1158px 1165px #fff, 
#                          668px 293px #fff, 1266px 199px #fff, 382px 493px #fff, 
#                          117px 484px #fff;
#             animation: animStar 100s linear infinite;
#         }
        
#         /* Main title with gradient and animation */
#         .main h1 {
#             font-family: 'Audiowide', cursive;
#             font-size: 4rem;
#             background: linear-gradient(90deg, #00dbde, #fc00ff, #00dbde);
#             background-size: 200% auto;
#             color: #000;
#             background-clip: text;
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             animation: shine 3s linear infinite;
#             text-shadow: 0 0 10px rgba(255,255,255,0.3);
#             margin-bottom: 0.5rem;
#             letter-spacing: 2px;
#         }
        
#         @keyframes shine {
#             to { background-position: 200% center; }
#         }
        
#         /* Subtitle with floating animation */
#         .main h2 {
#             font-family: 'Montserrat', sans-serif;
#             font-weight: 700;
#             color: #fff;
#             text-shadow: 0 0 10px rgba(0,255,255,0.7);
#             animation: float 6s ease-in-out infinite;
#             font-size: 1.8rem;
#         }
        
#         @keyframes float {
#             0% { transform: translateY(0px); }
#             50% { transform: translateY(-10px); }
#             100% { transform: translateY(0px); }
#         }
        
#         /* Sidebar with glass morphism effect */
#         section[data-testid="stSidebar"] {
#             background: rgba(15, 15, 15, 0.7) !important;
#             backdrop-filter: blur(10px);
#             -webkit-backdrop-filter: blur(10px);
#             border-right: 1px solid rgba(255, 255, 255, 0.1);
#             box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.36);
#         }
        
#         /* Sidebar title with neon effect */
#         section[data-testid="stSidebar"] h1 {
#             font-family: 'Orbitron', sans-serif;
#             color: #00ffff;
#             text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
#             font-size: 1.8rem;
#             letter-spacing: 1px;
#         }
        
#         /* Sidebar links with hover animation */
#         section[data-testid="stSidebar"] .css-1d391kg a {
#             font-family: 'Poppins', sans-serif;
#             color: #ffffff;
#             background: linear-gradient(90deg, rgba(0,219,222,0.1), rgba(252,0,255,0.1));
#             border-radius: 12px;
#             padding: 12px 20px;
#             margin: 8px 0;
#             transition: all 0.3s ease;
#             border-left: 3px solid transparent;
#             font-weight: 600;
#             letter-spacing: 0.5px;
#         }
        
#         section[data-testid="stSidebar"] .css-1d391kg a:hover {
#             border-left: 3px solid #00ffff;
#             background: linear-gradient(90deg, rgba(0,219,222,0.3), rgba(252,0,255,0.3));
#             transform: translateX(10px);
#             box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
#         }
        
#         /* File uploader styling */
#         .stFileUploader label div {
#             background: rgba(255, 255, 255, 0.1) !important;
#             border: 2px dashed rgba(0, 255, 255, 0.5) !important;
#             border-radius: 15px !important;
#             padding: 30px !important;
#             transition: all 0.3s ease !important;
#             color: white !important;
#         }
        
#         .stFileUploader label div:hover {
#             background: rgba(0, 255, 255, 0.1) !important;
#             border: 2px dashed rgba(0, 255, 255, 1) !important;
#             box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
#         }
        
#         /* Buttons with gradient and pulse animation */
#         button[kind="primary"] {
#             background: linear-gradient(90deg, #00dbde, #fc00ff) !important;
#             border: none !important;
#             border-radius: 50px !important;
#             color: white !important;
#             font-weight: 600 !important;
#             padding: 12px 24px !important;
#             font-family: 'Poppins', sans-serif !important;
#             letter-spacing: 1px !important;
#             box-shadow: 0 4px 15px rgba(0, 219, 222, 0.4) !important;
#             transition: all 0.3s ease !important;
#             position: relative !important;
#             overflow: hidden !important;
#         }
        
#         button[kind="primary"]:hover {
#             transform: translateY(-3px) !important;
#             box-shadow: 0 10px 20px rgba(0, 219, 222, 0.6) !important;
#         }
        
#         button[kind="primary"]:after {
#             content: "";
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.3));
#             transform: translateX(-100%);
#             transition: all 0.3s ease;
#         }
        
#         button[kind="primary"]:hover:after {
#             transform: translateX(100%);
#         }
        
#         /* Dataframe styling */
#         .stDataFrame {
#             border-radius: 15px !important;
#             overflow: hidden !important;
#             box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 10px;
#         }
        
#         ::-webkit-scrollbar-track {
#             background: rgba(255,255,255,0.05);
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb {
#             background: linear-gradient(#00dbde, #fc00ff);
#             border-radius: 10px;
#         }
        
#         /* Typewriter effect for info messages */
#         @keyframes typing {
#             from { width: 0 }
#             to { width: 100% }
#         }
        
#         @keyframes blink-caret {
#             from, to { border-color: transparent }
#             50% { border-color: #00ffff }
#         }
        
#         .typewriter {
#             overflow: hidden;
#             border-right: 2px solid #00ffff;
#             white-space: nowrap;
#             margin: 0 auto;
#             letter-spacing: 1px;
#             animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
#         }
        
#         /* Floating animation for cards */
#         @keyframes float-card {
#             0% { transform: translateY(0px); }
#             50% { transform: translateY(-10px); }
#             100% { transform: translateY(0px); }
#         }
        
#         .floating-card {
#             animation: float-card 6s ease-in-out infinite;
#         }
#     </style>
    
#     <!-- Starfield background -->
#     <div class="stars"></div>
# """, unsafe_allow_html=True)

# # ---------- App Config ----------
# st.set_page_config(
#     page_title="🚀 Onboarding Drop-off Analyzer | AI-Powered Insights",
#     layout="wide",
#     page_icon="📊",
#     initial_sidebar_state="expanded"
# )

# # ---------- Load Animations ----------
# lottie_analytics = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
# lottie_header = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_kdx6cani.json")
# lottie_upload = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_5tkzkblw.json")

# # ---------- Header Section with Animated Text ----------
# col1, col2 = st.columns([1, 2])

# with col1:
#     if lottie_analytics:
#         st_lottie(lottie_analytics, height=250, key="header-animation")

# with col2:
#     st.markdown("""
#     <h1>ONBOARDING DROP-OFF ANALYZER</h1>
#     <h2>AI-Powered User Journey Insights</h2>
#     """, unsafe_allow_html=True)
    
#     st.markdown("""
#     <div style="font-family: 'Poppins', sans-serif; font-size: 1.2rem; line-height: 1.6; color: #ffffffcc;">
#     Discover <span style="color: #00ffff; font-weight: 600;">hidden patterns</span> in your user onboarding flow. 
#     Upload your data and let our <span style="color: #fc00ff; font-weight: 600;">AI engine</span> identify 
#     exactly where and why users drop off.
#     </div>
#     """, unsafe_allow_html=True)

# # ---------- Animated Divider ----------
# st.markdown("""
# <div style="height: 2px; background: linear-gradient(90deg, transparent, #00dbde, #fc00ff, transparent); 
#             margin: 2rem 0; animation: rainbow 5s linear infinite; background-size: 400% 100%;"></div>

# <style>
#     @keyframes rainbow {
#         0% { background-position: 0% 50% }
#         100% { background-position: 100% 50% }
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------- File Upload Section with Animation ----------
# st.markdown("""
# <div class="floating-card" style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 2rem; 
#             backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); 
#             box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
# """, unsafe_allow_html=True)

# col_upload1, col_upload2 = st.columns([3, 1])

# with col_upload1:
#     uploaded_file = st.file_uploader(
#         "📤 UPLOAD YOUR ONBOARDING DATA (CSV)",
#         type="csv",
#         help="Upload your user journey data in CSV format"
#     )

# with col_upload2:
#     if lottie_upload:
#         st_lottie(lottie_upload, height=120, key="upload-animation")

# st.markdown("</div>", unsafe_allow_html=True)

# # ---------- Data Processing Section ----------
# if uploaded_file:
#     with st.spinner('✨ Analyzing your data with AI magic...'):
#         time.sleep(2)  # Simulate processing time
        
#         df = pd.read_csv(uploaded_file)
#         st.session_state.df = df
        
#         st.success("✅ Data successfully loaded and analyzed!")
        
#         # Animated success message
#         st.markdown("""
#         <div class="typewriter" style="font-family: 'Poppins', sans-serif; font-size: 1.2rem; 
#                     color: #39ff14; margin: 1rem 0;">
#         Discovered {:,} rows with {:,} unique user paths...
#         </div>
#         """.format(len(df), df['user_id'].nunique()), unsafe_allow_html=True)
        
#         # Display data with custom styling
#         st.markdown("""
#         <div style="margin-top: 2rem;">
#             <h3 style="font-family: 'Montserrat', sans-serif; color: #ffffff; 
#                 text-shadow: 0 0 10px rgba(0,255,255,0.5);">
#                 📊 DATA PREVIEW
#             </h3>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.dataframe(df.head().style
#                     .set_properties(**{'background-color': 'rgba(0,0,0,0.5)',
#                                       'color': 'white',
#                                       'border': '1px solid rgba(255,255,255,0.1)'})
#                     .highlight_max(color='rgba(0,219,222,0.3)')
#                     .highlight_min(color='rgba(252,0,255,0.3)'))
        
#         # Sample visualization (would be replaced with actual analysis)
#         st.markdown("""
#         <div style="margin-top: 2rem;">
#             <h3 style="font-family: 'Montserrat', sans-serif; color: #ffffff; 
#                 text-shadow: 0 0 10px rgba(0,255,255,0.5);">
#                 📈 DROP-OFF ANALYSIS
#             </h3>
#         </div>
#         """, unsafe_allow_html=True)
        
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.set_facecolor('none')
#         fig.patch.set_alpha(0.0)
        
#         # Sample data - replace with actual analysis
#         sample_data = pd.DataFrame({
#             'Step': ['Start', 'Step 1', 'Step 2', 'Step 3', 'Step 4', 'Complete'],
#             'Users': [1000, 750, 500, 300, 150, 50]
#         })
        
#         ax.plot(sample_data['Step'], sample_data['Users'], 
#                 color='#00ffff', linewidth=3, marker='o', markersize=10)
#         ax.fill_between(sample_data['Step'], sample_data['Users'], 
#                         color='rgba(0, 219, 222, 0.2)')
        
#         ax.set_xlabel('Onboarding Step', fontsize=12, color='white')
#         ax.set_ylabel('Remaining Users', fontsize=12, color='white')
#         ax.tick_params(colors='white')
        
#         for spine in ax.spines.values():
#             spine.set_edgecolor('rgba(255,255,255,0.3)')
        
#         st.pyplot(fig)
        
# else:
#     st.markdown("""
#     <div style="text-align: center; margin-top: 2rem; padding: 2rem; 
#                 background: rgba(255,255,255,0.05); border-radius: 15px;
#                 border: 1px dashed rgba(255,255,255,0.3);">
#         <h3 style="font-family: 'Poppins', sans-serif; color: rgba(255,255,255,0.7);">
#             ⚡ Upload your data to unlock powerful insights
#         </h3>
#         <p style="color: rgba(255,255,255,0.5);">
#             Our AI will analyze your onboarding funnel and identify optimization opportunities
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# # ---------- Footer with Animated Gradient ----------
# st.markdown("""
# <div style="height: 2px; background: linear-gradient(90deg, #fc00ff, #00dbde); 
#             margin: 3rem 0 1rem 0; width: 100%;"></div>

# <div style="text-align: center; color: rgba(255,255,255,0.5); font-family: 'Poppins', sans-serif;">
#     <p>🚀 Powered by AI | 💡 Visualized with Streamlit | 📊 Data Science at Your Fingertips</p>
#     <p style="font-size: 0.8rem;">© 2023 Onboarding Drop-off Analyzer | All Rights Reserved</p>
# </div>
# """, unsafe_allow_html=True)
