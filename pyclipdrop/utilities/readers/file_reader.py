from typing import Text
from pathlib import Path
from pyclipdrop.exceptions import FileOpenError


class FileReader:  
    @staticmethod
    def get_extension_from_file_path(file_path: Text) -> Text:
        return Path(file_path).suffix
    
    @staticmethod
    def get_data_from_file_path(file_path: Text) -> bytes:
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except (PermissionError, OSError) as e:
            raise FileOpenError("Error opening file: " + str(e)) from e