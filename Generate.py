import streamlit as st
import json
import google.generativeai as genai
from supabase import create_client, Client

st.set_page_config(
    page_title="Palette AI | Your Personalized Palette, Powered by AI",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://twitter.com/dotAadarsh',
        'Report a bug': "https://github.com/dotAadarsh/PaletteAI",
        'About': "Your Colors, Your Way. Powered by Google's Gemini AI & Supabase."
    })

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
url: str = SUPABASE_URL
key: str = SUPABASE_KEY
supabase: Client = create_client(url, key)

def save_to_supabase(color_palette, purpose, audience, theme, num_colors, user_input):
    # Insert the color palette into Supabase
    try:
        response = supabase.table('color_palette').insert({"purpose": purpose, "targeted_audience": audience, "theme": theme, "num_colors": num_colors,  "colors": color_palette, "user_input": user_input}).execute()
        st.success("Color palette saved successfully!")
    except Exception as e:
        st.error(f"Error saving color palette: {str(e)}")

@st.cache_resource 
def get_colors(prompt):

    genai.configure(api_key=GEMINI_API_KEY)

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    system_instruction = "You are a friendly assistant who helps in generating color palette based on the user's need. Return the colorName, hexCode & explanation."

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    result = json.loads(convo.last.text)
    
    return result


def display_color_palette(palette):
    # Display the color palette
    for color in palette:
        st.code(color['hexCode'])
        st.markdown(
            f"""
            <div style="background-color: {color['hexCode']}; width: 100px; height: 100px; border: 2px solid #555; border-radius: 10px;"></div>
            <p>{color['colorName']}</p>
            <p>{color['explanation']}</p>
            """,
            unsafe_allow_html=True
        )


def main():
    st.title("Palette AI 🎨")
    st.caption("Your Personalized Palette, Powered by AI")
    with st.sidebar:
        st.markdown("Submission for [Supabase Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)")
        st.info("Built on top of Gemini AI AND Supabase")
        
    color_palette = None
    # Initialize color palette in session state (empty list initially)
    if "color_palette" not in st.session_state:
        st.session_state["color_palette"] = []

    # Get user input
    col1, col2 = st.columns(2)
    with col1: 
        purpose = st.selectbox("Select Purpose", ["Website", "Mobile App", "Branding", "Marketing Material"])
        audience = st.selectbox("Select Targeted Audience", ["Youth Generation", "Professionals", "Children", "Elderly"])
    with col2:
        theme = st.selectbox("Select Theme", ["Minimalistic", "Playful", "Corporate", "Elegant"])
        num_colors = st.selectbox("Select Number of Colors", [3, 4, 5, 6])
    
    user_input = st.text_input("Elaborate to get the desired result")
    
    final_prompt =  f"Purpose: {purpose}\nTargeted Audience: {audience}\nTheme: {theme}\nColors: {num_colors}\nAdditional info: {user_input}"

    # Generate button for generating color palette
    if st.button("Generate Color Palette"):
        color_palette = get_colors(final_prompt)
        if color_palette:
            st.session_state["color_palette"] = color_palette  # Update session state
            st.write("Generated Color Palette ✨:")

    # Check if color palette exists in session state
    if st.session_state["color_palette"]:
        color_palette = st.session_state["color_palette"]  # Retrieve from session state
        st.write("Generated Color Palette ✨:")
        display_color_palette(color_palette)

    # Save button with conditional logic based on color palette availability
    if color_palette:
        if st.button("Save Color Palette"):
            save_to_supabase(color_palette, purpose, audience, theme, num_colors, user_input)

if __name__ == "__main__":
    main()
