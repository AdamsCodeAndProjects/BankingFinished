class NegativeAmountInAccountException(Exception):
    def __init__(self, message):
        self.message = message


class DepositingNegativeValuesException(Exception):
    def __init__(self, message):
        self.message = message


class TooMuchMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeWithdrawException(Exception):
    def __init__(self, message):
        self.message = message
