import requests
from pathlib import Path
from urllib.parse import urlparse
from typing import Text, List, Tuple


class InputUtilities:
    @staticmethod
    def get_data_and_suffix(input_file: Text, supported_extensions: List[Text] = None) -> Tuple[bytes, Text]:
        if FileUtilities.is_valid_file_path(input_file):
            input_suffix = FileUtilities.get_suffix_from_file_path(input_file)
            image_data = FileUtilities.get_data_from_file_path(input_file)

        elif URLUtilities.is_valid_url(input_file):
            input_suffix = URLUtilities.get_suffix_from_url(input_file)
            image_data = URLUtilities.get_data_from_url(input_file)

        else:
            raise ValueError("Input file must be a valid file path or URL.")

        if supported_extensions and input_suffix not in supported_extensions:
            raise ValueError(f"Input file must have one of the following extensions: {', '.join(supported_extensions)}")

        return image_data, input_suffix
    

class OutputUtilities:
    @staticmethod
    def validate_output_file(output_file: Text, supported_extensions: List[Text] = None) -> Text:
        if FileUtilities.is_valid_parent_directory(output_file):
            output_suffix = FileUtilities.get_suffix_from_file_path(output_file)

        else:
            raise ValueError("The path to the output file does not exist.")
        
        if supported_extensions and output_suffix not in supported_extensions:
            raise ValueError(f"Output file must have one of the following extensions: {', '.join(supported_extensions)}")


class URLUtilities:
    @staticmethod
    def is_valid_url(url: Text) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except AttributeError:
            return False
    
    @staticmethod
    def get_suffix_from_url(url: Text) -> Text:
        return Path(urlparse(url).path).suffix
    
    @staticmethod
    def get_data_from_url(url: Text) -> bytes:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    

class FileUtilities:
    @staticmethod
    def is_valid_file_path(file_path: Text) -> bool:
        return Path(file_path).exists()
    
    def is_valid_parent_directory(file_path: Text) -> bool:
        return Path(file_path).parent.exists()
    
    @staticmethod
    def get_suffix_from_file_path(file_path: Text) -> Text:
        return Path(file_path).suffix
    
    @staticmethod
    def get_data_from_file_path(file_path: Text) -> bytes:
        with open(file_path, 'rb') as file:
            return file.read()