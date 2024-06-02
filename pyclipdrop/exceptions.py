
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


class URLParseError(Exception):
    """
    Exception raised for errors in parsing a URL.
    """
    pass


class URLInvalidError(Exception):
    """
    Exception raised for when a URL is invalid.
    """
    pass


class URLDownloadError(Exception):
    """
    Exception raised for errors in downloading content from a URL.
    """
    pass


class ValueOutOfRangeError(Exception):
    """
    Exception raised when an input is out of an expected range.
    """
    pass


class ValueTooLongError(Exception):
    """
    Exception raised when an input is too long.
    """
    pass