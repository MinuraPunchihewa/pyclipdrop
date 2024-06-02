from typing import Text
from urllib.parse import urlparse


class URLValidator:
    @staticmethod
    def is_valid_url(url: Text) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except AttributeError:
            return False
