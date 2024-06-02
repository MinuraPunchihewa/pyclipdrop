from PIL import Image
from io import BytesIO
from pyclipdrop.exceptions import FileResolutionError, FileSizeError


class ImageContentValidator:
    @staticmethod
    def exceeds_max_resolution(image_bytes: bytes, max_megapixels: int) -> bool:
        with Image.open(BytesIO(image_bytes)) as image:
            # Calculate the total number of pixels in the image
            total_pixels = image.width * image.height

            # Convert total pixels to megapixels
            total_megapixels = total_pixels / 1_000_000

            # Check if the total megapixels exceeds the maximum
            if total_megapixels > max_megapixels:
                raise FileResolutionError(f"Input image must have a resolution of {max_megapixels} megapixels or less.")
        

    @staticmethod
    def exceeds_max_file_size(image_bytes: bytes, max_megabytes: int) -> bool:
        # Convert bytes to megabytes
        total_megabytes = len(image_bytes) / 1_000_000

        # Check if the total megabytes exceeds the maximum
        if total_megabytes > max_megabytes:
            raise FileSizeError(f"Input image must have a size of {max_megabytes} megabytes or less.")
        
    @staticmethod
    def exceeds_max_width(image_bytes: bytes, max_pixels_width: int) -> bool:
        with Image.open(BytesIO(image_bytes)) as image:
            if image.width > max_pixels_width:
                raise FileResolutionError(f"Input image must have a width of {max_pixels_width} pixels or less.")
            
    @staticmethod
    def exceeds_max_height(image_bytes: bytes, max_pixels_height: int) -> bool:
        with Image.open(BytesIO(image_bytes)) as image:
            if image.height > max_pixels_height:
                raise FileResolutionError(f"Input image must have a height of {max_pixels_height} pixels or less.")