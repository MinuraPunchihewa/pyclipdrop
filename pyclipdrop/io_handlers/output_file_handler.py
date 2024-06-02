from typing import Text, List
from pyclipdrop.utilities import FileValidator, FileReader, FileWriter


class OutputFileHandler:
    def __init__(self, output_file: Text, supported_extensions: List[Text] = None) -> None:
        self.output_file = output_file
        self.supported_extensions = supported_extensions + ['.jpeg'] if '.jpg' in supported_extensions else supported_extensions
        self.output_extension = None

    def validate(self) -> None:
        if FileValidator.is_valid_parent_directory(self.output_file):
            self.output_extension = FileReader.get_extension_from_file_path(self.output_file)

        else:
            raise ValueError("The path to the output file does not exist.")
        
        if self.supported_extensions and self.output_extension not in self.supported_extensions:
            raise ValueError(f"Output file must have one of the following extensions: {', '.join(self.supported_extensions)}")
        
    def write_data(self, data: bytes) -> None:
        FileWriter.write_data_to_file_path(self.output_file, data)