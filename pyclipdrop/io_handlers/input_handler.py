from typing import Text, List
from pyclipdrop.utilities import URLUtilities, FileUtilities, ExtensionUtilities


class InputHandler:
    def __init__(self, input_file: Text, supported_extensions: List[Text] = None) -> None:
        self.input_file = input_file
        self.supported_extensions =  supported_extensions + ['.jpeg'] if '.jpg' in supported_extensions else supported_extensions
        self.input_extension = None
        self.is_file = None

    def validate(self) -> None:
        if FileUtilities.is_valid_file_path(self.input_file):
            self.input_extension = FileUtilities.get_suffix_from_file_path(self.input_file)
            self.is_file = True

        elif URLUtilities.is_valid_url(self.input_file):
            self.input_extension = URLUtilities.get_suffix_from_url(self.input_file)
            self.is_file = False

        else:
            raise ValueError("Input file must be a valid file path or URL.")

        if self.supported_extensions and self.input_extension not in self.supported_extensions:
            raise ValueError(f"Input file must have one of the following extensions: {', '.join(self.supported_extensions)}")
        
    def get_data(self) -> bytes:
        if self.is_file:
            return FileUtilities.get_data_from_file_path(self.input_file)
        else:
            return URLUtilities.get_data_from_url(self.input_file)
        
    def get_extension(self) -> Text:
        return self.input_extension
