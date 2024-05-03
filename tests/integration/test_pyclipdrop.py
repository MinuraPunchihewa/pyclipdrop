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


if __name__ == '__main__':
    unittest.main()