import os
import io
import requests
from typing import Text, Dict

from pyclipdrop.settings import settings
from pyclipdrop.utilities import InputUtilities, OutputUtilities


class ClipdropClient:
    """
    The client class for the Clipdrop API.

    Args:
        api_key (Text): The API key for the Clipdrop API.
        base_url (Text): The base URL for the Clipdrop API. The default value is maintained in the settings module.
        version (Text): The version of the Clipdrop API to use. The default value is maintained in the settings module.

    Raises:
        ValueError: If the API key is not passed to the client or set as an environment variable.
    """

    def __init__(self, api_key: Text = None, base_url: Text = settings.BASE_URL, version: Text = settings.VERSION) -> None:
        self.api_key = api_key or os.environ.get('CLIPDROP_API_KEY')
        if not self.api_key:
            raise ValueError("A Clipdrop API key must either be passed to the client or set as an environment variable.")

        self.base_url = base_url
        self.version = version

    def text_to_image(self, prompt: Text, output_file: Text = 'output.png') -> None:
        """
        Generate an image from a text prompt.

        Args:
            prompt (Text): The text prompt to generate the image from.
            output_file (Text): The name of the output file. The default value is 'output.png'. The only supported extension is PNG.

        Raises:
            ValueError: If the path to the output file is not valid or the extension is not PNG.
            requests.exceptions.HTTPError: If the API request fails.        
        """

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.png']).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/text-to-image/{self.version}',
            files={
                'prompt': (None, prompt, 'text/plain')
            }
        )

        self._save_response(response, output_file)

    def replace_background(self, input_file: Text, prompt: Text, output_file: Text = None):
        """
        Replace the background of an image with a new background.

        Args:
            input_file (Text): The name of the input file. The supported extensions are PNG, JPG, and WEBP.
            prompt (Text): The text prompt to generate the new background from.
            output_file (Text): The name of the output file. The default value is 'output' with the same extension as the input file.The extension of the output file must match the extension of the input file.

        Raises:
            ValueError: If the input file does not exist or the extension is not supported.
            ValueError: If the path to the output file is not valid or the extension does not match that of the input file.
            requests.exceptions.HTTPError: If the API request fails.       
        """

        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # If the output file is not specified, use 'output' with the same extension as the input file
        if not output_file:
            output_file = f'output{input_suffix}'

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=[input_suffix]).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/replace-background/{self.version}',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}')
            },
            data={
                'prompt': prompt
            }
        )

        self._save_response(response, output_file)
        
    def remove_background(self, input_file: Text, output_file: Text = 'output.png'):
        """
        Remove the background of an image.

        Args:
            input_file (Text): The name of the input file. The supported extensions are PNG, JPG, and WEBP.
            output_file (Text): The name of the output file. The default value is 'output.png'. The supported extensions are PNG, JPG, and WEBP.

        Raises:
            ValueError: If the input file does not exist or the extension is not supported.
            ValueError: If the path to the output file is not valid or the extension is not supported.
            requests.exceptions.HTTPError: If the API request fails.
        """

        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.png', '.jpg', '.webp']).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/remove-background/{self.version}',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}')
            }
        )

        self._save_response(response, output_file)

    def remove_text(self, input_file: Text, output_file: Text = 'output.png'):
        """
        Remove the text from an image.

        Args:
            input_file (Text): The name of the input file. The supported extensions are PNG or JPG
            output_file (Text): The name of the output file. The default value is 'output.png'. The only supported extension is PNG.

        Raises:
            ValueError: If the input file does not exist or the extension is not supported.
            ValueError: If the path to the output file is not valid or the extension is not PNG.
            requests.exceptions.HTTPError: If the API request fails.
        """

        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg']).get_data_and_suffix()

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.png']).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/remove-text/{self.version}',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}')
            }
        )

        self._save_response(response, output_file)

    def reimagine(self, input_file: Text, output_file: Text = 'output.jpg'):
        """
        Reimagine an image.

        Args:
            input_file (Text): The name of the input file. The supported extensions are PNG, JPG, and WEBP.
            output_file (Text): The name of the output file. The default value is 'output.jpg'. The only supported extension is JPG.

        Raises:
            ValueError: If the input file does not exist or the extension is not supported.
            ValueError: If the path to the output file is not valid or the extension is not supported.
            requests.exceptions.HTTPError: If the API request fails.
        """

        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.jpg']).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/reimagine/{self.version}/reimagine',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}')
            }
        )

        self._save_response(response, output_file)

    def sketch_to_image(self, input_file: Text, prompt: Text, output_file: Text = 'output.png'):
        """
        Generate an image from a sketch.

        Args:
            input_file (Text): The name of the input file. The supported extensions are PNG, JPG, and WEBP.
            prompt (Text): The text prompt describing the image to generate.
            output_file (Text): The name of the output file. The default value is 'output.jpg'. The only supported extension is JPG.

        Raises:
            ValueError: If the input file does not exist or the extension is not supported.
            ValueError: If the path to the output file is not valid or the extension is not PNG.
            requests.exceptions.HTTPError: If the API request fails.
        """

        # get input data and suffix if the input file is valid
        image_data, input_suffix = InputUtilities(input_file, supported_extensions=['.png', '.jpg', '.webp']).get_data_and_suffix()

        # Check if the output file is valid
        OutputUtilities(output_file, supported_extensions=['.jpg']).validate_output_file()

        response = self._submit_request(
            f'{self.base_url}/sketch-to-image/{self.version}/sketch-to-image',
            files={
                'image_file': (input_file, image_data, f'image/{input_suffix[1:]}'),
                'prompt': (None, prompt, 'text/plain')
            }
        )

        self._save_response(response, output_file)

    def _submit_request(self, url: Text, files: Dict, data: Dict = None) -> requests.Response:
        """
        Submit a request to the Clipdrop API.

        Args:
            endpoint (Text): The endpoint of the API to submit the request to.
            files (Dict): A dictionary of files to submit with the request.
            data (Dict): A dictionary of data to submit with the request.

        Returns:
            requests.Response: The response object from the API request.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        response = requests.post(
            url,
            files=files,
            data=data,
            headers={
                'x-api-key': self.api_key
            }
        )

        response.raise_for_status()

        return response
    
    def _save_response(self, response: requests.Response, output_file: Text) -> None:
        """
        Save the content of a response object to a file.

        Args:
            response (requests.Response): The response object to save.
            output_file (Text): The name of the output file.
        """

        with open(output_file, 'wb') as f:
            f.write(response.content)