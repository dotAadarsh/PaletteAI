# Palette AI 🎨

**Your Personalized Palette, Powered by AI**

## Introduction

Palette AI is a web application that generates personalized color palettes powered by AI. It is developed as a submission for the [Supabase Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon).

The color palette is generated based on the purpose, targeted audience, theme, and additional information provided by the user. The generated color palette can be saved to the Supabase database for future reference.

## Built With

- [Streamlit](https://streamlit.io/)
- [Gemini AI](https://ai.google.dev/)
- [Supabase](https://supabase.io/)

## Features

- **Generate Color Palette:** Users can generate a color palette by providing information about the purpose, targeted audience, theme, and additional comments.
- **Save Color Palette:** Generated color palettes can be saved to the Supabase database for future reference.
- **Responsive Design:** The web application is designed to be responsive and user-friendly.
- **Exploration:** A page to search the generated color palettes.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python
- Pip
- [Supabase | The Open Source Firebase Alternative](https://supabase.com/)
- [Streamlit • A faster way to build and share data apps](https://streamlit.io/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dotAadarsh/PaletteAI.git
   ```

2. Install the packages
	```sh
	pip install -r requirements.txt
	```
3. Add your secret keys in the `.streamlit/secrets.toml`file
    ```
    [secrets]
    GEMINI_API_KEY = "<YOUR_GEMINI_API_KEY>"
    SUPABASE_URL = "<YOUR_SUPABASE_URL>"
    SUPABASE_KEY = "<YOUR_SUPABASE_KEY>"
    ```

4. Run the application
    ```
    streamlit run app.py
    ```

### Usage
- Select purpose, targeted audience, theme, and the number of colors.
- Provide additional information in the text input if needed.
- Click on Generate Color Palette.
- The generated color palette will be displayed.
- Click on Save Color Palette to save the palette to the Supabase database.
