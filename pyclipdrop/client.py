import requests
from typing import Text
from pathlib import Path


class PyClipdropClient:
    def __init__(self, api_key: Text):
        self.api_key = api_key

    def text_to_image(self, prompt: Text, output_file: Text = 'output.png'):
        output_path = Path(output_file)

        # Check if the output file has a .png extension
        if output_path.suffix != '.png':
            raise ValueError("Output file must be a .png file.")
        
        # Check if the path to the file exists
        if not output_path.parent.exists():
            raise ValueError("The path to the output file does not exist.")

        response = requests.post(
            'https://clipdrop-api.co/text-to-image/v1',
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
        

    