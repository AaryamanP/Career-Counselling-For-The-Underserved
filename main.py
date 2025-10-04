import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load local .env if present (keeps secrets out of source)
load_dotenv()

# 🗝️ Configure your Groq API Key (read from environment; do NOT hard-code)
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment; set it before running")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
)

st.set_page_config(page_title="Career Guidance", page_icon="🎯", layout="centered")
st.title("🎯 Inclusive Career Guidance")
st.write("Get personalized career suggestions based on your strengths, preferences, and needs.")

# 🌟 Form Inputs
with st.form("career_form"):
    conditions = st.multiselect(
        "Do you have any diagnosed conditions?",
        ["Dyslexia", "Autism Spectrum", "ADHD", "Physical disability", "Other"]
    )

    activities = st.multiselect(
        "What type of activities do you enjoy most? (Pick top 2)",
        ["Working with hands", "Creative arts", "Helping/caring for people/animals",
         "Solving puzzles/math/logic problems", "Organizing or managing things",
         "Technology", "Outdoor/Nature-related activities"]
    )

    work_style = st.radio(
        "How do you prefer to work?",
        ["Alone, at my own pace", "In a small, quiet group", "In a team with clear roles", "Flexible (mix of solo & group)"]
    )

    environment = st.radio(
        "What environment suits you best?",
        ["Quiet, structured", "Active, hands-on", "Outdoors/nature", "Creative/artistic space"]
    )

    routine_preference = st.radio(
        "Do you enjoy routine or variety in tasks?",
        ["Strong routine", "Mix of routine and new tasks", "Always new challenges"]
    )

    strengths = st.multiselect(
        "What are you good at? (Pick top 3)",
        ["Attention to detail", "Creativity/artistic skills", "Problem-solving",
         "Physical coordination", "Memorizing facts/details", "Communicating", "Technology"]
    )

    learning_style = st.radio(
        "How do you learn best?",
        ["Visually", "By doing", "Listening", "Written instructions"]
    )

    challenges = st.multiselect(
        "What challenges do you face at work/school? (Pick 1-2)",
        ["Reading/writing tasks", "Social interactions", "Focusing for long periods",
         "Physical tasks", "Unstructured tasks"]
    )

    job_values = st.multiselect(
        "What’s most important in a job? (Pick top 2)",
        ["Flexibility in hours", "Clear instructions", "Helping others",
         "Creativity/freedom", "Stable income"]
    )

    career_interest = st.text_input("Any careers you’re curious about? (Optional)")

    submitted = st.form_submit_button("🔍 Get Career Suggestions")

# 🧠 AI Suggestion
if submitted:
    st.info("Analyzing your answers with AI...")
    user_data = f"""
    Conditions: {', '.join(conditions)}
    Activities enjoyed: {', '.join(activities)}
    Work preference: {work_style}
    Best environment: {environment}
    Routine preference: {routine_preference}
    Strengths: {', '.join(strengths)}
    Learning style: {learning_style}
    Challenges: {', '.join(challenges)}
    Job values: {', '.join(job_values)}
    Career interests: {career_interest}
    """

    prompt = f"""
    You are a compassionate career counselor. Based on the user's strengths, preferences, and challenges, suggest 2-3 inclusive and accessible career paths. The user may have disabilities and deserves thoughtful, strengths-based guidance.

    {user_data}
    """

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=500
        )
        result = response.choices[0].message.content
        st.success("Here are some career paths you might enjoy:")
        st.markdown(result)
    except Exception as e:
        st.error(f"Error: {e}")
