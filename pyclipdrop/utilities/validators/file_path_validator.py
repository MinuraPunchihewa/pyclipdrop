from typing import Text
from pathlib import Path


class FilePathValidator:
    @staticmethod
    def is_valid_file_path(file_path: Text) -> bool:
        return Path(file_path).exists()
    
    @staticmethod
    def is_valid_parent_directory(file_path: Text) -> bool:
        return Path(file_path).parent.exists()
