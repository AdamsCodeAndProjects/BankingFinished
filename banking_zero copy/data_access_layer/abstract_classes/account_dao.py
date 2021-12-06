# customer data access object
from abc import ABC, abstractmethod
from typing import List

from entities.accounts import Account


class AccountDataAccessObject(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, account_id: int, receiving_account_id: int,
                                                     transfer_amount: int) -> List[Account]:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id) -> bool:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def get_all_customer_accounts_by_id(self, customer_id) -> List[Account]:
        pass
