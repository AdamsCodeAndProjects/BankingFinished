from abc import ABC

from data_access_layer.abstract_classes.account_dao import AccountDataAccessObject
from entities.accounts import Account
from typing import List


# cust ID, acct ID, amount in account, number of accounts

class AccountDAOImp(AccountDataAccessObject, ABC):
    account_one = Account(1, 1, 10)  # Used by selected_account
    account_two = Account(2, 2, 200)  # Used by deposit
    account_three = Account(3, 3, 50)  # Used by withdraw
    account_four = Account(4, 4, 200)  # Used by transfer
    account_six = Account(4, 6, 800)  # transfer
    account_five = Account(5, 5, 50000)  # Duplicate ID

    account_list = [account_one, account_two, account_three, account_four, account_five, account_six]
    account_id_generator = 6
    same_customer_account_dict = {}

    def create_account(self, account: Account) -> Account:
        new_account = account
        new_account.account_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(new_account)
        return new_account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

    def deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                account.amount_in_account += deposit
                return account

    def withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                if account.amount_in_account >= withdraw:
                    account.amount_in_account = account.amount_in_account - withdraw
                else:
                    print("You do not have that much money in your account")
                return account

    # FIX ME
    def transfer_money_between_accounts_by_their_ids(self, account_id: int,  transfer_amount: int) -> Account:
        pass
        # for account in AccountDAOImp.same_customer_account_dict:
        #     if account.customer_id == customer_id:
        #         if account.amount_in_account >= transfer_amount:

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                index = AccountDAOImp.account_list.index(account)
                del AccountDAOImp.account_list[index]
                return True

    def get_all_customer_accounts_by_id(self, customer_id) -> List[Account]:
        for account in AccountDAOImp.account_list:
            if account.customer_id == customer_id:
                return AccountDAOImp.account_list

    def get_all_accounts(self) -> List[Account]:
        pass

