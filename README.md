# Palette AI 🎨

**Your Personalized Palette, Powered by AI**

![PaletteAI](https://github.com/dotAadarsh/PaletteAI/assets/71810927/2563c15e-a344-4d75-9d4e-1a197995bece)

## Introduction

Palette AI is a web application that generates personalized color palettes powered by AI. It is developed as a submission for the [Supabase Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon).

The color palette is generated based on the purpose, targeted audience, theme, and additional information provided by the user. The generated color palette can be saved to the Supabase database for future reference.

## Built With

- [Streamlit](https://streamlit.io/)
- [Gemini AI](https://ai.google.dev/)
- [Supabase](https://supabase.io/)
- [Hugging Face](https://huggingface.co/)

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
- Use the Explore tab to find all the generated color palettes

## SQL Definition

![SQL Defition](https://github.com/dotAadarsh/PaletteAI/assets/71810927/481a8fcd-95f7-44cd-a152-afd8ddc20f33)

## Supabase Edge Function

You can find the code that is deployed to generate the image in the functions/text-to-image/index.ts file. 

Explanation: This Deno script sets up an HTTP server that converts text prompts into images using the Hugging Face Inference library. It imports the `serve` function from the Deno standard library for HTTP server and the `HfInference` class from the Hugging Face Inference library. After parsing the JSON data from the request, it uses the Hugging Face Inference library to convert the received text prompt into an image, employing the model 'stabilityai/stable-diffusion-2' and disabling caching. Finally, it returns the converted image as the response.

This code is deployed to the Supabase Edge Function. A seprate URL is generated once deployed which we can access it to generate the image.

Read this [Hugging Face Inference API](https://supabase.com/docs/guides/ai/hugging-face) for more info. Note: You need to add the Hugging Face API. 

## Exploring PGroonga: Multilingual Full Text Search

So I though of implement a full text search for the generated color palette. PGroonga is a PostgreSQL extension adding a full text search indexing method based on Groonga. Follow [PGroonga: Multilingual Full Text Search](https://supabase.com/docs/guides/database/extensions/pgroonga) guide to know how to use this. Here is the screenshot of its implementation on Supabase SQL Editor.

![SQL-Editor](https://github.com/dotAadarsh/PaletteAI/assets/71810927/57bc68f1-3b10-4568-a29c-34e36586d79a)






