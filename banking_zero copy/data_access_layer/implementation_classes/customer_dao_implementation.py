# from data_access_layer.abstract_classes.customer_dao import CustomerDataAccessObject
from data_access_layer.abstract_classes.customer_dao import CustomerDataAccessObject
from data_access_layer.implementation_classes.account_dao_implementation import AccountDAOImp
from entities.accounts import Account
from entities.customers import Customer
from typing import List


class CustomerDAOImp(CustomerDataAccessObject):
    # new customers for testing purposes
    new_customer = Customer("Average", "Joe", 21200, 1)
    new_customer_two = Customer("Plain", "Jane", 30502, 2)
    deleted_customer = Customer("Elvis", "Presley", 10865, 3)

    # will possibly be used in the database
    customer_list = [new_customer, new_customer_two, deleted_customer]
    customer_id_generator = 8

    def create_customer_entry(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(customer)
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            # When the customer Id matches the customer Id added in the function
            if customer.customer_id == customer_id:
                return customer

    def update_customer_by_id(self, customer_id: int) -> Customer:
        # Iterate through list of customers to find the correct customer
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index_one = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index_one] = customer_id
                return customer_in_list

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customers_in_list in CustomerDAOImp.customer_list:
            if customers_in_list.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customers_in_list)
                del CustomerDAOImp.customer_list[index]
                return bool

    def get_all_customers_information(self) -> List[Customer]:
        return CustomerDAOImp.customer_list






