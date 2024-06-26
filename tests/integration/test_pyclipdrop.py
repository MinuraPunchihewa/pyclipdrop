import os
import glob
import unittest

from pyclipdrop import ClipdropClient


class TestClipdropClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ClipdropClient()

    def tearDown(self) -> None:
        files = glob.glob('tests/integration/output/*')
        for f in files:
            os.remove(f)

    def test_text_to_image(self):
        self.client.text_to_image(prompt='shot of vaporwave fashion dog in miami', output_file='tests/integration/output/output.png')

        self.assertTrue(os.path.exists('tests/integration/output/output.png'))

    def test_replace_background(self):
        self.client.replace_background(
            input_file='tests/integration/input/wine.jpg',
            prompt='a cozy marble kitchen with wine glasses',
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_remove_background(self):
        self.client.remove_background(
            input_file='tests/integration/input/car.jpg',
            output_file='tests/integration/output/output.png'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.png'))

    def test_remove_text(self):
        self.client.remove_text(
            input_file='tests/integration/input/billboard.jpg',
            output_file='tests/integration/output/output.png'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.png'))

    def test_reimagine(self):
        self.client.reimagine(
            input_file='tests/integration/input/apartment.webp',
            output_file='tests/integration/output/output.jpeg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpeg'))

    def test_sketch_to_image(self):
        self.client.sketch_to_image(
            input_file='tests/integration/input/owl.png',
            prompt='an owl on a branch, cinematic',
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_uncrop(self):
        self.client.uncrop(
            input_file='tests/integration/input/wine.jpg',
            extend_up=200,
            extend_down=200,
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_image_upscaling(self):
        self.client.image_upscaling(
            input_file='tests/integration/input/apartment.webp',
            target_height=1000,
            target_width=1000,
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_cleanup(self):
        self.client.cleanup(
            input_file='tests/integration/input/jeep_in_desert.jpg',
            mask_file='tests/integration/input/jeep_in_desert_mask.png',
            output_file='tests/integration/output/output.png'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.png'))

    def test_portrait_depth_estimation(self):
        self.client.portrait_depth_estimation(
            input_file='tests/integration/input/portrait.jpg',
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_portrait_surface_normals(self):
        self.client.portrait_surface_normals(
            input_file='tests/integration/input/portrait.jpg',
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))

    def test_text_inpainting(self):
        self.client.text_inpainting(
            input_file='tests/integration/input/woman_in_scarf.jpg',
            mask_file='tests/integration/input/woman_in_scarf_mask.png',
            prompt='A woman with a red scarf',
            output_file='tests/integration/output/output.jpg'
        )

        self.assertTrue(os.path.exists('tests/integration/output/output.jpg'))
    

if __name__ == '__main__':
    unittest.main()