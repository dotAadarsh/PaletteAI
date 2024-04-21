import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def display_color_palette(color_list):
    st.sidebar.json(color_list, expanded=False)
    # Display the color palette
    for palette_item in color_list:
        with st.expander(f"Color pallete: {palette_item['id']}"):
            colors = palette_item["colors"]
            for color in colors:
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

    # Fetch all colors from Supabase
    try:
        response = supabase.table('color_palette').select("*").execute()
        palette_data = response.data
    except Exception as e:
        st.error(f"Error fetching colors: {str(e)}")
        palette_data = []  # Empty list in case of error

    if palette_data:
        st.header("All Saved Color Palettes")
        display_color_palette(palette_data)
    else:
        st.info("No color palettes found.")

if __name__ == "__main__":
    main()

