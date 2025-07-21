import requests
import pandas as pd
from textblob import TextBlob

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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

def static_tip(step):
    tips = {
        "signup": "Simplify the signup form and allow social login.",
        "email_verification": "Add clear instructions and resend OTP option.",
        "profile_setup": "Minimize required fields or allow skipping.",
        "feature_tour": "Provide a skip button and shorten the tour.",
        "first_action": "Guide users with tooltips or a quick task.",
        "upgrade_prompt": "Delay the upgrade prompt until value is shown."
    }
    return tips.get(step, "Consider simplifying or explaining this step better.")
