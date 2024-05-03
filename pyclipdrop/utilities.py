from pathlib import Path
from typing import Text, Bool
from urllib.parse import urlparse


class URLUtilities:
    @staticmethod
    def is_valid_url(url: Text) -> Bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except AttributeError:
            return False
    
    @staticmethod
    def get_suffix_from_url(url: Text) -> Text:
        return Path(urlparse(url).path).suffix
    

class FileUtilities:
    @staticmethod
    def is_valid_file_path(file_path: Text) -> Bool:
        return Path(file_path).exists()
    
    @staticmethod
    def get_suffix_from_file_path(file_path: Text) -> Text:
        return Path(file_path).suffix