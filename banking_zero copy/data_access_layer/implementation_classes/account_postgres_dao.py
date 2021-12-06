from typing import List
from data_access_layer.abstract_classes.account_dao import AccountDataAccessObject
from entities.accounts import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDataAccessObject):
    def create_account(self, account: Account) -> Account:
        sql = "insert into account values(%s, default, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.customer_id, account.amount_in_account))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

#
    def deposit_into_account_by_id(self, account_id: int, deposit: int) -> Account:
        sql = "update account set amount_in_account = amount_in_account + %s where account_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (deposit, account_id))
        connection.commit()
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

#
    def withdraw_from_account_by_id(self, account_id: int, withdraw: int) -> Account:
        sql = "update account set amount_in_account = amount_in_account - %s where account_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (withdraw, account_id))
        connection.commit()
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

#
    def transfer_money_between_accounts_by_their_ids(self, account_id: int, receiving_account_id: int,
                                                     transfer_amount: int) -> List[Account]:
        sql = "update account set amount_in_account = amount_in_account - %s where account_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_amount, account_id))
        sql = "update account set amount_in_account = amount_in_account + %s where account_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_amount, receiving_account_id))
        connection.commit()
        transferred_account = cursor.fetchall()
        my_transfer_list = []
        for transfer in transferred_account:
            my_transfer_list.append(Account(*transfer))
        return my_transfer_list

    def delete_account_by_id(self, account_id) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    def get_all_accounts(self) -> List[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list

    def get_all_customer_accounts_by_id(self, customer_id: int) -> List[Account]:
        sql = "select * from account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list
