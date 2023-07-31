import os
import openai


os.getenv('OPENAI_API_KEY')


class ImageGenerator:

    def __init__(self, text_prompt: str) -> None:
        self.text_prompt = text_prompt


    # Function to generate images from text using DALL-E
    
    def generate_image_from_text(self) -> str:
        try:    
            response = openai.Image.create(
                model="image-alpha-001",
                prompt=self.text_prompt,
                n=1,  # Number of images to generate
            )
            return response['data'][0]['url']
        
        except Exception as e:
            print(e)