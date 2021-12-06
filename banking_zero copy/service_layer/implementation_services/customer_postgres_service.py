from abc import ABC
from typing import List

from custom_exceptions.duplicate_exceptions import DuplicateCustomerIDException, NoIdFoundException
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.abstract_services.customer_service import CustomerService


# Don't need to write tests for, just call the DAO itself

class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for existing_customer in customers:
            if existing_customer.customer_id == customer.customer_id:
                raise DuplicateCustomerIDException("Customer ID taken by another")
        created_customer = self.customer_dao.create_customer_entry(customer)
        return created_customer

    def service_update_customer_by_id(self, customer_id: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for current_customer in customers:
            if current_customer.customer_id == customer_id:
                raise DuplicateCustomerIDException("Customer ID taken by another")
        updated_customer = self.customer_dao.update_customer_by_id(customer_id)
        return updated_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)

    def service_get_all_customers_information(self) -> List[Customer]:
        return self.customer_dao.get_all_customers_information()
