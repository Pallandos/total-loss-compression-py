import google.generativeai as genai
from PIL import Image
from openai import OpenAI
import requests
import os

def compress(image_path: str, gemini_api_key: str, prompt: str = "Describe this image in a detailed and effective way.") -> str:
    """
    Compress an image by sending it to the Gemini AI and returns its description.
    
    Args:
        image_path (str): The local path to the image (e.g., 'photo.jpg').
        gemini_api_key (str): Your Google Gemini API key.
        prompt (str): The instruction given to the AI.
        
    Returns:
        str: The text description of the image. It will be used to unzip the image
    """
    # Configure the Google API
    genai.configure(api_key=gemini_api_key)
    
    # Use the Flash model (very fast and excellent for vision tasks)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Send the image and prompt to Gemini
        response = model.generate_content([prompt, img])
        return response.text
        
    except FileNotFoundError:
        return f"Error: The image '{image_path}' was not found."
    except Exception as e:
        return f"An error occurred with Gemini: {e}"


def unzip(description: str, openai_api_key: str, save_path: str = "generated_image.png") -> str:
    """
    Unzip an image based on its description and saves it to the local disk.
    
    Args:
        description (str): tlc text of your image.
        openai_api_key (str): Your OpenAI API key.
        save_path (str): The output file path and name.
        
    Returns:
        str: A success message with the file path.
    """
    # Initialize the OpenAI client
    client = OpenAI(api_key=openai_api_key)
    
    try:
        # Request generation from DALL-E 3
        response = client.images.generate(
            model="dall-e-3",
            prompt=description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Retrieve the URL of the generated image
        image_url = response.data[0].url
        
        # Download the image
        image_data = requests.get(image_url).content
        
        # Save it to the disk
        with open(save_path, 'wb') as file:
            file.write(image_data)
            
        return f"Success! Image generated and saved as: {save_path}"
        
    except Exception as e:
        return f"An error occurred during image generation: {e}"