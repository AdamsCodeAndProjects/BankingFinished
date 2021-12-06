# customer data access object
from abc import ABC, abstractmethod
from typing import List

from entities.accounts import Account
from entities.customers import Customer


class CustomerDataAccessObject(ABC):

    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # get customer info
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # update info
    @abstractmethod
    def update_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # delete info
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_customers_information(self) -> List[Customer]:
        pass


