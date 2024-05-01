import os
import requests
from typing import Text
from pathlib import Path

from pyclipdrop.settings import settings


class PyClipdropClient:
    def __init__(self, api_key: Text = None, base_url: Text = settings.BASE_URL, version: Text = settings.VERSION):
        self.api_key = api_key or os.environ.get('CLIPDROP_API_KEY')
        if not self.api_key:
            raise ValueError("A Clipdrop API key must either be passed to the client or set as an environment variable.")

        self.base_url = base_url
        self.version = version

    def text_to_image(self, prompt: Text, output_file: Text = 'output.png'):
        output_path = Path(output_file)

        # Check if the output file has a .png extension
        if output_path.suffix != '.png':
            raise ValueError("Output file must be a .png file.")
        
        # Check if the path to the file exists
        if not output_path.parent.exists():
            raise ValueError("The path to the output file does not exist.")

        response = requests.post(
            f'{self.base_url}/text-to-image/{self.version}',
            files={
                'prompt': (None, prompt, 'text/plain')
            },
            headers={
                'x-api-key': self.api_key
            }
        )

        if (response.ok):
            with open(output_file, 'wb') as f:
                f.write(response.content)
        else:
            response.raise_for_status()

    def remove_background(self, image_path: Text, prompt: Text, output_file: Text = 'output.png'):
        output_path = Path(output_file)

        # Check if the output file has a .png or .webp extension
        suffix = output_path.suffix
        if suffix not in ['.png', '.jpg', '.webp']:
            raise ValueError("Output file must be a .png, .jpg or .webp file.")
        
        # Check if the path to the file exists
        if not output_path.parent.exists():
            raise ValueError("The path to the output file does not exist.")

        response = requests.post(
            f'{self.base_url}/remove-background/{self.version}',
            files={
                'image_file': (image_path, open(image_path, 'rb'), f'image/{suffix[1:]}')
            },
            data={
                'prompt': prompt
            },
            headers={
                'x-api-key': self.api_key
            }
        )

        if (response.ok):
            with open(output_file, 'wb') as f:
                f.write(response.content)
        else:
            response.raise_for_status()
        

    