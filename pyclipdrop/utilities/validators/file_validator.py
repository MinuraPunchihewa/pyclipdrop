from typing import Text
from pathlib import Path
from pyclipdrop.exceptions import FileExtensionUnsupportedError


class FileValidator:
    @staticmethod
    def is_valid_file_path(file_path: Text) -> bool:
        return Path(file_path).exists()
    
    @staticmethod
    def is_valid_parent_directory(file_path: Text) -> bool:
        return Path(file_path).parent.exists()
    
    @staticmethod
    def is_valid_file_extension(file_extension: Text, supported_extensions: Text) -> bool:
        supported_extensions = supported_extensions + ['.jpeg'] if '.jpg' in supported_extensions else supported_extensions
        if not file_extension in supported_extensions:
            raise FileExtensionUnsupportedError(f"Input file must have one of the following extensions: {', '.join(supported_extensions)}")
