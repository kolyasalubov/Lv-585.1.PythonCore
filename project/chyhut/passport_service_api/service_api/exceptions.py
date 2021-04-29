class ApiError(Exception):
    """
    Class for representing of custom API errors.

    This class can contain the next attributes:
     * status_code: int - integer number that represent HTTP status code
     * data: dict - data for representing of HTTP error body
    """

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)

        if status_code is not None:
            self.status_code = status_code


class UnprocessableEntityError(ApiError):
    status_code = 422


class AuthorizationError(ApiError):
    status_code = 401


class NotFoundError(ApiError):
    status_code = 404
