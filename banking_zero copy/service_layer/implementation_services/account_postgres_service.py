from custom_exceptions.AccountExceptions import DepositingNegativeValuesException, NegativeAmountInAccountException, \
    TooMuchMoneyException, NegativeWithdrawException
from custom_exceptions.duplicate_exceptions import DuplicateAccountIDException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities import accounts
from entities.accounts import Account
from service_layer.abstract_services.account_service import AccountService
from typing import List


class AccountPostgresService(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        accounts_listing = self.account_dao.get_all_accounts()
        for existing_account in accounts_listing:
            if existing_account.account_id == account.account_id:
                raise DuplicateAccountIDException("Account ID taken by another")
        created_account = self.account_dao.create_account(account)
        return created_account

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        if deposit < 0:
            raise DepositingNegativeValuesException("You cannot deposit negative amounts")
        if deposit > 1000000000:
            raise TooMuchMoneyException("You have to split this amount between multiple accounts")
        return self.account_dao.deposit_into_account_by_id(account_id, deposit)

    def service_withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        account_access = self.account_dao.get_account_by_id(account_id)
        if account_access.account_id == account_id:
            if account_access.amount_in_account < withdraw:
                raise NegativeAmountInAccountException("You cannot have negative amounts of money in your account")
            if withdraw < 0:
                raise NegativeWithdrawException("You cannot withdraw negative amounts")
            return self.account_dao.withdraw_from_account_by_id(account_id, withdraw)

    def service_transfer_money_between_accounts_by_their_ids(self, account_id: int, receiving_account_id: int,
                                                             transfer_amount: int) -> List[Account]:
        account_access = self.account_dao.get_account_by_id(account_id)
        receiving_account = self.account_dao.get_account_by_id(receiving_account_id)
        if account_access.amount_in_account < transfer_amount:
            raise NegativeAmountInAccountException("You cannot have negative amounts of money in your account")
        if transfer_amount < 0:
            raise NegativeWithdrawException("You cannot withdraw negative amounts")
        return self.account_dao.transfer_money_between_accounts_by_their_ids(account_access.account_id,
                                                                             receiving_account.account_id,
                                                                             transfer_amount)

    def service_delete_account_by_id(self, account_id) -> bool:
        return self.account_dao.delete_account_by_id(account_id)

    def service_get_all_accounts(self) -> List[Account]:
        return self.account_dao.get_all_accounts()

    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        # account_access = self.customer_dao.get_customer_by_id(customer_id)
        # if account_access.customer_id == customer_id:
        return self.account_dao.get_all_customer_accounts_by_id(customer_id)
        # return self.account_dao.get_all_customer_accounts_by_id(customer_id)
