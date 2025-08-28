from google import genai
from google.genai import types
from PIL import Image
import io
from dotenv import load_dotenv
import os
from io import BytesIO

load_dotenv()
gemini_api_key = os.getenv("API_KEY") #getting the api key from the dotenv

gemini_client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    #converting the image from raw to byte stored on memory
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()
    response = gemini_client.models.generate_content(model='gemini-2.5-flash', contents=[types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'), 'Caption this image'])
    return response.text