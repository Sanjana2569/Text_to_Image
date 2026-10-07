import io
import urllib.parse
import requests
from PIL import Image
import streamlit as st

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("Text to Image Generator")

user_prompt = st.text_input("Enter your prompt:", placeholder="e.g., A cute cat wearing sunglasses")

if st.button("Generate Image"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating your image... please wait a few seconds."):
            try:
                # Format prompt for the open public endpoint (no API key needed)
                clean_prompt = urllib.parse.quote(user_prompt)
                image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}"
                
                # Fetch image
                response = requests.get(image_url, timeout=45)
                
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption=user_prompt, use_container_width=True)
                else:
                    st.error("Server is busy. Please try again.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")