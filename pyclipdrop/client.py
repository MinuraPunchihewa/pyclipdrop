import os
import io
import requests
from typing import Text
from pathlib import Path

from pyclipdrop.settings import settings
from pyclipdrop.utilities import InputUtilities, OutputUtilities


# TODO: Add docstrings
class PyClipdropClient:
    def __init__(self, api_key: Text = None, base_url: Text = settings.BASE_URL, version: Text = settings.VERSION):
        self.api_key = api_key or os.environ.get('CLIPDROP_API_KEY')
        if not self.api_key:
            raise ValueError("A Clipdrop API key must either be passed to the client or set as an environment variable.")

        self.base_url = base_url
        self.version = version

    def text_to_image(self, prompt: Text, output_file: Text = 'output.png'):
        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.png']).validate_output_file()

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
        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # If the output file is not specified, use 'output' with the same extension as the input file
        if not output_file:
            output_file = f'output{input_suffix}'

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=[input_suffix]).validate_output_file()

        response = requests.post(
            f'{self.base_url}/replace-background/{self.version}',
            files={
                'image_file': (input_file, io.BytesIO(image_data), f'image/{input_suffix[1:]}')
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
        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.png', '.jpg', '.webp']).validate_output_file()

        response = requests.post(
            f'{self.base_url}/remove-background/{self.version}',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}')
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