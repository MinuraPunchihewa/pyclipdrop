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