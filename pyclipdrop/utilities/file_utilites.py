from typing import Text
from pathlib import Path


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