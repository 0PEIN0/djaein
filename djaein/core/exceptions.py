from .exception_type import ExceptionType


class BaseException(Exception):

    def __init__(self,
                 code):
        super().__init__()
        self.error_type = ExceptionType.BASE
        self.custom_code = code

    class Meta:
        abstract = True


class DatabaseGetException(BaseException):

    def __init__(self,
                 code):
        super().__init__(code=code)
        self.error_type = ExceptionType.DATABASE_GET
