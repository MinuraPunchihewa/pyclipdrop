from PIL import Image
from io import BytesIO


class ImageContentValidator:
    @staticmethod
    def exceeds_max_resolution(image_bytes: bytes, max_megapixels: int) -> bool:
        with Image.open(BytesIO(image_bytes)) as image:
            # Calculate the total number of pixels in the image
            total_pixels = image.width * image.height

            # Convert total pixels to megapixels
            total_megapixels = total_pixels / 1_000_000

            # Check if the total megapixels exceeds the maximum
            return total_megapixels > max_megapixels
        

    @staticmethod
    def exceeds_max_file_size(image_bytes: bytes, max_megabytes: int) -> bool:
        # Convert bytes to megabytes
        total_megabytes = len(image_bytes) / 1_000_000

        # Check if the total megabytes exceeds the maximum
        return total_megabytes > max_megabytes