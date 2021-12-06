from abc import ABC
from typing import List

from custom_exceptions.duplicate_exceptions import DuplicateAccountIDException
from data_access_layer.implementation_classes.account_dao_implementation import AccountDAOImp
from data_access_layer.implementation_classes.customer_dao_implementation import CustomerDAOImp
from entities.accounts import Account
from service_layer.abstract_services.account_service import AccountService


class AccountServiceImp(AccountService, ABC):
    def __init__(self, account_dao: AccountDAOImp):
        self.account_dao: AccountDAOImp = account_dao

    def service_create_account(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account_id == account.account_id:
                raise DuplicateAccountIDException("You cannot have duplicate account IDs")
        new_account = self.account_dao.create_account(account)
        return new_account

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        return self.account_dao.deposit_into_account_by_id(account_id, deposit)

    def service_withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        return self.account_dao.withdraw_from_account_by_id(account_id, withdraw)

    def service_transfer_money_between_accounts_by_their_ids(self, account_id: int, receiving_account_id: int,
                                                             transfer_amount: int) -> List[Account]:
        return self.account_dao.transfer_money_between_accounts_by_their_ids(account_id, transfer_amount)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        return self.account_dao.delete_account_by_id(account_id)
