from PIL import Image
from io import BytesIO


class ImageValidator:
    @staticmethod
    def exceeds_max_resolution(image_bytes: bytes, max_megapixels: int) -> bool:
        with Image.open(BytesIO(image_bytes)) as image:
            # Calculate the total number of pixels in the image
            total_pixels = image.width * image.height

            # Convert total pixels to megapixels
            total_megapixels = total_pixels / 1_000_000

            # Check if the total megapixels exceeds the maximum
            return total_megapixels > max_megapixels