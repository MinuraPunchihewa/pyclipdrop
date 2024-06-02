
class APIRequestError(Exception):
    """
    Exception raised for errors in the API request to Clipdrop.
    """
    pass


class FileOpenError(Exception):
    """
    Exception raised for errors in opening a file.
    """
    pass


class FileWriteError(Exception):
    """
    Exception raised for errors in writing to a file.
    """
    pass