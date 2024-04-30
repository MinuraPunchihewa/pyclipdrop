from pydantic_settings import BaseSettings


class PyClipdropSettings(BaseSettings):
    """
    Settings for the PyClipdrop package.

    Attributes
    ----------

    BASE_URL : str
        Base URL for the Clipdrop API.

    VERSION : str
        Version of the Clipdrop API.
    """

    BASE_URL = "https://clipdrop-api.co"
    VERSION = "v1"
