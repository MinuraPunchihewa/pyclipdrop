from typing import Text
from pyclipdrop.exceptions import FileOpenError, FileWriteError


class FileWriter:
    @staticmethod
    def write_data_to_file_path(file_path: Text, data: bytes) -> None:
        try:
            with open(file_path, 'wb') as f:
                try:
                    f.write(data)
                except (IOError, OSError) as e:
                    raise FileWriteError("Error writing to file: " + str(e)) from e
        except (PermissionError, OSError) as e:
            raise FileOpenError("Error opening file: " + str(e)) from e