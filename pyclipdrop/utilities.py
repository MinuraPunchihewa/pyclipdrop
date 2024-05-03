import requests
from pathlib import Path
from urllib.parse import urlparse
from typing import Text, List, Tuple


class InputUtilities:
    def __init__(self, input_file: Text, supported_extensions: List[Text] = None) -> None:
        self.input_file = input_file
        self.supported_extensions = supported_extensions

    def get_data_and_suffix(self) -> Tuple[bytes, Text]:
        if FileUtilities.is_valid_file_path(self.input_file):
            input_suffix = FileUtilities.get_suffix_from_file_path(self.input_file)
            image_data = FileUtilities.get_data_from_file_path(self.input_file)

        elif URLUtilities.is_valid_url(self.input_file):
            input_suffix = URLUtilities.get_suffix_from_url(self.input_file)
            image_data = URLUtilities.get_data_from_url(self.input_file)

        else:
            raise ValueError("Input file must be a valid file path or URL.")

        if self.supported_extensions and input_suffix not in self.supported_extensions:
            raise ValueError(f"Input file must have one of the following extensions: {', '.join(self.supported_extensions)}")

        return image_data, input_suffix
    

class OutputUtilities:
    def __init__(self, output_file: Text, supported_extensions: List[Text] = None) -> None:
        self.output_file = output_file
        self.supported_extensions = supported_extensions

    def validate_output_file(self) -> Text:
        if FileUtilities.is_valid_parent_directory(self.output_file):
            output_suffix = FileUtilities.get_suffix_from_file_path(self.output_file)

        else:
            raise ValueError("The path to the output file does not exist.")
        
        if self.supported_extensions and output_suffix not in self.supported_extensions:
            raise ValueError(f"Output file must have one of the following extensions: {', '.join(self.supported_extensions)}")


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