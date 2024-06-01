from typing import Text, List
from pyclipdrop.utilities import FileUtilities


class OutputHandler:
    def __init__(self, output_file: Text, supported_extensions: List[Text] = None) -> None:
        self.output_file = output_file
        self.supported_extensions = supported_extensions + ['.jpeg'] if '.jpg' in supported_extensions else supported_extensions
        self.output_extension = None

    def validate(self) -> None:
        if FileUtilities.is_valid_parent_directory(self.output_file):
            self.output_extension = FileUtilities.get_suffix_from_file_path(self.output_file)

        else:
            raise ValueError("The path to the output file does not exist.")
        
        if self.supported_extensions and self.output_extension not in self.supported_extensions:
            raise ValueError(f"Output file must have one of the following extensions: {', '.join(self.supported_extensions)}")
