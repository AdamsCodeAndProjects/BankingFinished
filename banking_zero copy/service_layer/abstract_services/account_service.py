from abc import ABC, abstractmethod
from typing import List

from entities.accounts import Account
from entities.customers import Customer


class AccountService(ABC):

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        pass

    @abstractmethod
    def service_withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        pass

    @abstractmethod
    def service_transfer_money_between_accounts_by_their_ids(self, account_id: int, receiving_account_id: int,
                                                             transfer_amount: int) -> List[Account]:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        pass

    @abstractmethod
    def service_get_all_accounts(self) -> List[Account]:
        pass
