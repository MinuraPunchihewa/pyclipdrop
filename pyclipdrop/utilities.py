import requests
from typing import Text
from pathlib import Path
from urllib.parse import urlparse


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