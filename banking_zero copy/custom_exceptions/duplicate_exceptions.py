class DuplicateAccountIDException(Exception):
    def __init__(self, message):
        self.message = message


class DuplicateCustomerIDException(Exception):
    def __init__(self, message):
        self.message = message


class NoIdFoundException(Exception):
    def __init__(self, message):
        self.message = message
