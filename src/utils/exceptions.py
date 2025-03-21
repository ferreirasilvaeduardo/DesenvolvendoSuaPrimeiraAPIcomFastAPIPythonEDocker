class BaseException(Exception):  # Renamed to avoid conflict
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message


class NotFoundException(BaseException):  # Updated to inherit from the renamed class
    message = "Not Found"
