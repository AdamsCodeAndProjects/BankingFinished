from abc import ABC, abstractmethod
from typing import List

from entities.customers import Customer


# happy path

class CustomerService(ABC):

    @abstractmethod
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # delete info
    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def service_get_all_customers_information(self) -> List[Customer]:
        pass
