
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


class InputValidationError(Exception):
    """
    Exception raised for errors in validating the inputs passed to the various methods.
    """
    pass


class ValueOutOfRangeError(InputValidationError):
    """
    Exception raised when an input is out of an expected range.
    """
    pass


class ValueTooLongError(InputValidationError):
    """
    Exception raised when an input is too long.
    """
    pass