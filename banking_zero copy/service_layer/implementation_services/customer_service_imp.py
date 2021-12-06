from abc import ABC

from custom_exceptions.duplicate_exceptions import DuplicateAccountIDException, DuplicateCustomerIDException
from data_access_layer.implementation_classes.customer_dao_implementation import CustomerDAOImp
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService
from typing import List


class CustomerServiceImp(CustomerService, ABC):
    def __init__(self, customer_dao):

        self.customer_dao: CustomerDAOImp = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            # if they have the same account_id, and if they are different customers, EXCEPTION
            if current_customer.customer_id == customer.customer_id:
                if current_customer.date_of_birth != customer.date_of_birth \
                        and current_customer.last_name != customer.last_name:
                    raise DuplicateCustomerIDException("Customer ID is taken by another!")
            else:
                return self.customer_dao.create_customer_entry(customer)

    # get customer info
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    # get all customers info
    # def service_get_all_customers_information(self) -> List[Customer]:
    #     return self.customer_dao.get_all_customers_information()

    # update info.   He did jersey number instead of customer_id here
    # def service_update_customer_by_id(self, customer_id: int) -> Customer:
        # for current_customer in self.customer_dao.customer_list:
        #     if they have the same account_id, but not customer IDs, and if their DOBs match, then raise an
        #     exception.  Otherwise, return the customer ID

        # if current_customer.account_id == account_id:
        #     if current_customer.customer_id != customer_id:
        #         if current_customer.date_of_birth == customer.date_of_birth:
        #             raise DuplicateAccountNumberException("Account Number is taken by another!")
        # return self.customer_dao.update_customer_by_id(customer_id)

    # delete info
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)
