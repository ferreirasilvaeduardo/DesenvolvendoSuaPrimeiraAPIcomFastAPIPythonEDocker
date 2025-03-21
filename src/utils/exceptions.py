class BaseException(Exception):  # Renamed to avoid conflict
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message


class NotFoundException(BaseException):  # Updated to inherit from the renamed class
    message = "Not Found"


class InsertionException(Exception):
    def __init__(self, message: str = "Error inserting product"):
        self.message = message
        super().__init__(self.message)


class UpdateException(Exception):
    def __init__(self, message: str = "Error updating product"):
        self.message = message
        super().__init__(self.message)
