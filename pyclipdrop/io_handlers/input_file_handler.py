from typing import Text, List
from pyclipdrop.exceptions import FileOrURLInvalidError
from pyclipdrop.utilities import URLValidator, FileValidator, ImageContentValidator, URLReader, FileReader


class InputFileHandler:
    def __init__(self, input_file: Text, supported_extensions: List[Text] = None, max_resolution: int = None, max_size: int = None, max_width: int = None, max_height: int = None) -> None:
        self.input_file = input_file
        self.supported_extensions = supported_extensions
        self.max_resolution = max_resolution
        self.max_size = max_size
        self.max_width = max_width
        self.max_height = max_height
        self.input_extension = None
        self.is_file = None
        self.image_data = None

    def validate(self) -> None:
        if FileValidator.is_valid_file_path(self.input_file):
            self.input_extension = FileReader.get_extension_from_file_path(self.input_file)
            self.is_file = True

        elif URLValidator.is_valid_url(self.input_file):
            self.input_extension = URLReader.get_extension_from_url(self.input_file)
            self.is_file = False

        else:
            raise FileOrURLInvalidError("Input file must be a valid file path or URL.")
        
        if self.supported_extensions:
            FileValidator.is_valid_file_extension(self.input_extension, self.supported_extensions)

        if self.max_resolution or self.max_size or self.max_width or self.max_height:
            image_data = self.get_data()

            if self.max_resolution:
                ImageContentValidator.exceeds_max_resolution(image_data, self.max_resolution)

            if self.max_size:
                ImageContentValidator.exceeds_max_resolution(image_data, self.max_size)

            if self.max_width:
                ImageContentValidator.exceeds_max_width(image_data, self.max_width)

            if self.max_height:
                ImageContentValidator.exceeds_max_height(image_data, self.max_height)
        
    def get_data(self) -> bytes:
        if self.image_data is None:       
            if self.is_file:
                self.image_data = FileReader.get_data_from_file_path(self.input_file)
            else:
                self.image_data = URLReader.get_data_from_url(self.input_file)

        return self.image_data
        
    def get_extension(self) -> Text:
        return self.input_extension
