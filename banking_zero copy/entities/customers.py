class Customer:
    def __init__(self, first_name: str, last_name: str, date_of_birth: int, customer_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.customer_id = customer_id

    def make_customer_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "dateOfBirth": self.date_of_birth,
            "customerId": self.customer_id
        }

    def __str__(self):
        return "first name {} " \
               "last name {}" \
               "date of birth {}" \
               "customer ID {}".format(self.first_name, self.last_name, self.date_of_birth,
                                       self.customer_id)
