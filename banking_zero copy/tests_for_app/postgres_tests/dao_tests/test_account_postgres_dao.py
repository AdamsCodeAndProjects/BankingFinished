from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.accounts import Account

account_dao = AccountPostgresDAO()

new_account = Account(4, 9, 200)
delete_account = Account(5, 88, 678)
depositing_account = Account(6, 8, 880)
new_withdraw_account = Account(5, 28, 9999)


def test_create_account_success():
    account_result = account_dao.create_account(new_account)
    assert account_result.amount_in_account != 0


def test_get_account_by_id_success():
    initial_account = account_dao.get_account_by_id(2)
    assert initial_account.account_id == 2


def test_deposit_into_account_by_id_success():
    deposited_account = account_dao.deposit_into_account_by_id(depositing_account.account_id, 5)
    assert deposited_account.amount_in_account > 1800


def test_withdraw_from_account_by_id_success():
    withdraw_account: Account = account_dao.withdraw_from_account_by_id(new_withdraw_account.account_id, 5)
    assert withdraw_account.amount_in_account < 9999


def test_transfer_money_between_accounts_by_their_ids_success():
    transferring_account: Account = account_dao.transfer_money_between_accounts_by_their_ids(
        depositing_account.account_id, 3, 1)
    assert transferring_account.amount_in_account >= 8000008


def test_delete_account_by_id_success():
    to_be_deleted = account_dao.create_account(delete_account)
    assert account_dao.delete_account_by_id(to_be_deleted.account_id)


def test_get_all_accounts_success():
    accounts = account_dao.get_all_accounts()
    assert len(accounts) >= 3


def test_get_all_customer_accounts_by_id_success():
    accounts = account_dao.get_all_customer_accounts_by_id(4)
    assert len(accounts) >= 3
