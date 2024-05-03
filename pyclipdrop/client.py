import os
import requests
from typing import Text
from pathlib import Path

from pyclipdrop.settings import settings
from pyclipdrop.utilities import FileUtilities, URLUtilities


# TODO: Add docstrings
# TODO: Remove duplicate code
# TODO: Suppport URL input
class PyClipdropClient:
    def __init__(self, api_key: Text = None, base_url: Text = settings.BASE_URL, version: Text = settings.VERSION):
        self.api_key = api_key or os.environ.get('CLIPDROP_API_KEY')
        if not self.api_key:
            raise ValueError("A Clipdrop API key must either be passed to the client or set as an environment variable.")

        self.base_url = base_url
        self.version = version

    def text_to_image(self, prompt: Text, output_file: Text = 'output.png'):
        # Check if the path to the file exists
        if not FileUtilities.is_valid_parent_directory(output_file):
            raise ValueError("The path to the output file does not exist.")

        # Check if the output file has a .png extension
        if FileUtilities.get_suffix_from_file_path(output_file) != '.png':
            raise ValueError("Output file must be a .png file.")

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

    def replace_background(self, input_file: Text, prompt: Text, output_file: Text = None):
        input_path = Path(input_file)
        input_suffix = input_path.suffix

        # If the output file is not specified, use 'output' with the same extension as the input file
        if not output_file:
            output_file = f'output{input_suffix}'

        output_path = Path(output_file)
        output_suffix = output_path.suffix

        # Check if the input file exists
        if not input_path.exists():
            raise ValueError("The input file does not exist.")

        # Check if the input file has a .png, .jpg or .webp extension
        if input_suffix not in ['.png', '.jpg', '.webp']:
            raise ValueError("Output file must be a .png, .jpg or .webp file.")
        
        # Check if the output file has the same extension as the input file
        if output_suffix != input_suffix:
            raise ValueError("Output file must have the same extension as the input file.")
        
        # Check if the path to the output file exists
        if not output_path.parent.exists():
            raise ValueError("The path to the output file does not exist.")

        with open(input_file, 'rb') as image_file:
            response = requests.post(
                f'{self.base_url}/replace-background/{self.version}',
                files={
                    'image_file': (input_file, image_file, f'image/{input_suffix[1:]}')
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
        
    def remove_background(self, input_file: Text, output_file: Text = 'output.png'):
        input_path = Path(input_file)
        input_suffix = input_path.suffix

        output_path = Path(output_file)
        output_suffix = output_path.suffix

        # Check if the input file exists
        if not input_path.exists():
            raise ValueError("The input file does not exist.")

        # Check if the input file has a .png, .jpg or .webp extension
        if input_suffix not in ['.png', '.jpg', '.webp']:
            raise ValueError("Output file must be a .png, .jpg or .webp file.")
        
        # Check if the output file has a .png, .jpg or .webp extension
        if output_suffix not in ['.png', '.jpg', '.webp']:
            raise ValueError("Output file must be a .png, .jpg or .webp file.")
        
        # Check if the path to the output file exists
        if not output_path.parent.exists():
            raise ValueError("The path to the output file does not exist.")

        with open(input_file, 'rb') as image_file:
            response = requests.post(
                f'{self.base_url}/remove-background/{self.version}',
                files={
                    'image_file': (input_file, image_file, f'image/{input_suffix[1:]}')
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