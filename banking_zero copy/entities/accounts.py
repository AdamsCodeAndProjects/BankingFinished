class Account:
    def __init__(self, customer_id: int, account_id: int, amount_in_account: int):
        self.customer_id = customer_id
        self.account_id = account_id
        self.amount_in_account = amount_in_account

    def __str__(self):
        return "customerId {}," "accountId {}," \
               "amountInAccount {},".format(self.customer_id, self.account_id,
                                            self.amount_in_account)

    def make_account_dictionary(self):
        return {
            "customerId": self.customer_id,
            "accountId": self.account_id,
            "amountInAccount": self.amount_in_account
        }
