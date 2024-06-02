import requests
from typing import Text
from pathlib import Path
from urllib.parse import urlparse
from pyclipdrop.exceptions import URLParseError, URLDownloadError


class URLReader:  
    @staticmethod
    def get_extension_from_url(url: Text) -> Text:
        try:
            return Path(urlparse(url).path).suffix
        except ValueError as e:
            raise URLParseError("Failed to parse URL") from e
    
    @staticmethod
    def get_data_from_url(url: Text) -> bytes:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            raise URLDownloadError("Failed to download content from URL") from e