from google import genai
from PIL import Image
import io

def compress(image_path: str, gemini_api_key: str, prompt: str = "Describe this image in a detailed and effective way.") -> str:
    """
    Compress an image by sending it to the Gemini AI and returns its description.
    
    Args:
        image_path (str): The local path to the image (e.g., 'photo.jpg').
        gemini_api_key (str): Your Google API key.
        prompt (str): The instruction given to the AI.
        
    Returns:
        str: The text description of the image. It will be used to unzip the image.
    """
    client = genai.Client(api_key=gemini_api_key)
    
    try:
        img = Image.open(image_path)
        
        response = client.models.generate_content(
            model='gemini-3-pro-image',
            contents=[prompt, img]
        )
        return response.text
        
    except FileNotFoundError:
        return f"Error: The image '{image_path}' was not found."
    except Exception as e:
        return f"An error occurred with Gemini: {e}"


def unzip(description: str, gemini_api_key: str, save_path: str = "generated_image.png") -> str:
    """
    Unzip an image based on its description using Google Imagen 3 and saves it to the local disk.
    
    Args:
        description (str): tlc text of your image.
        gemini_api_key (str): Your Google API key (same as for compress).
        save_path (str): The output file path and name.
        
    Returns:
        str: A success message with the file path.
    """
    client = genai.Client(api_key=gemini_api_key)
    
    try:
        # On utilise maintenant 'generate_content' de manière universelle
        response = client.models.generate_content(
            model='imagen-3.0-generate-001',
            contents=description,
        )
        
        # Le chemin pour récupérer les bytes de l'image a changé avec cette méthode
        image_bytes = response.candidates[0].content.parts[0].inline_data.data
        
        # Conversion des bytes en image Pillow et sauvegarde
        image = Image.open(io.BytesIO(image_bytes))
        image.save(save_path)
            
        return f"Success! Image generated and saved as: {save_path}"
        
    except Exception as e:
        return f"An error occurred during image generation: {e}"