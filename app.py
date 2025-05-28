import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# --- Setup ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="OpenAI Prompt Tester", layout="centered")

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #105e94;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Interactive Prompt Playground")

# --- Session state for responses ---
if "results" not in st.session_state:
    st.session_state.results = []

# --- UI Form ---
with st.form("chat_form"):
    system_prompt = st.text_input("System Prompt", value="You're an expert product reviewer!")
    user_prompt = st.text_area("User Prompt", value="Hey, what's latest iPhone model?")

    col1, col2 = st.columns(2)
    with col1:
        model = st.selectbox("Model", options=["gpt-3.5-turbo", "gpt-4o"])
        temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
        max_tokens = st.slider("Max Tokens", 10, 300, 50, 10)
    with col2:
        frequency_penalty = st.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)
        presence_penalty = st.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.1)

    stop_sequence = st.text_input("Stop Sequence(s), comma-separated", value="")

    submitted = st.form_submit_button("Generate")

# --- Handle Submission ---
if submitted:
    stop = [s.strip() for s in stop_sequence.split(",")] if stop_sequence else None

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop
        )

        answer = response.choices[0].message.content.strip()

        # Store result in session
        st.session_state.results.append({
            "Model": model,
            "Temperature": temperature,
            "Max Tokens": max_tokens,
            "Frequency Penalty": frequency_penalty,
            "Presence Penalty": presence_penalty,
            "Output": answer
        })

    except Exception as e:
        st.error(f"API Error: {e}")

# --- Display Full Output Table with Wide Output Column ---
if st.session_state.results:
    st.subheader("📋 Output Summary")

    table_html = """
    <div style= padding: 1rem;">
        <table style="width: 100%; border-collapse: collapse; font-family: 'Segoe UI', sans-serif; color: white;">
            <thead style="background-color: #1f77b4;">
                <tr>
                    <th style="padding: 8px; text-align: left;">Model</th>
                    <th style="padding: 8px; text-align: right; width: 60px;">Temp</th>
                    <th style="padding: 8px; text-align: right; width: 80px;">Max Tokens</th>
                    <th style="padding: 8px; text-align: right; width: 80px;">Freq.</th>
                    <th style="padding: 8px; text-align: right; width: 80px;">Pres.</th>
                    <th style="padding: 8px; text-align: left; min-width: 400px;">Output</th>
                </tr>
            </thead>
            <tbody>
    """

    for row in st.session_state.results:
        table_html += f"""
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="padding: 8px;">{row['Model']}</td>
                <td style="padding: 8px; text-align: right;">{row['Temperature']}</td>
                <td style="padding: 8px; text-align: right;">{row['Max Tokens']}</td>
                <td style="padding: 8px; text-align: right;">{row['Frequency Penalty']}</td>
                <td style="padding: 8px; text-align: right;">{row['Presence Penalty']}</td>
                <td style="padding: 8px; white-space: pre-wrap;">{row['Output']}</td>
            </tr>
        """

    table_html += """
            </tbody>
        </table>
    </div>
    """

    # ✅ Use HTML renderer instead of markdown to fix rendering issue
    st.components.v1.html(table_html, height=600, scrolling=True)


    # --- Reflections Text Area ---
st.subheader("🧠 Your Reflections")

# Initialize reflection state
if "reflection_text" not in st.session_state:
    st.session_state.reflection_text = ""

st.text_area(
    "Write your thoughts, analysis, or notes here:",
    key="reflection_text",
    height=300,
    placeholder="Type your detailed reflection on what changed and why..."
)

