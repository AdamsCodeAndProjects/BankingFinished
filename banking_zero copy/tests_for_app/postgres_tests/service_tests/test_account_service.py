from custom_exceptions.AccountExceptions import NegativeAmountInAccountException, DepositingNegativeValuesException, \
    TooMuchMoneyException, NegativeWithdrawException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.accounts import Account
from service_layer.implementation_services.account_postgres_service import AccountPostgresService

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)
poor_man = Account(12, 12, -500000)


def test_catch_account_from_over_withdrawing_balance():
    try:
        account_service.service_withdraw_from_account_by_id(2, 9999)
        assert False
    except NegativeAmountInAccountException as e:
        assert str(e) == "You cannot have negative amounts of money in your account"


def test_catch_withdrawing_negative_amounts():
    try:
        account_service.service_withdraw_from_account_by_id(4, -500)
        assert False
    except NegativeWithdrawException as e:
        assert str(e) == "You cannot withdraw negative amounts"


def test_catch_account_from_depositing_negative_amount_in_account():
    try:
        account_service.service_deposit_into_account_by_id(4, -500)
        assert False
    except DepositingNegativeValuesException as e:
        assert str(e) == "You cannot deposit negative amounts"


def test_catch_deposit_overload():
    try:
        account_service.service_deposit_into_account_by_id(4, 500000000000000000000000)
        assert False
    except TooMuchMoneyException as e:
        assert str(e) == "You have to split this amount between multiple accounts"


def test_catch_over_transferring_amounts():
    try:
        account_service.service_transfer_money_between_accounts_by_their_ids(2, 4, 10000)
        assert False
    except NegativeAmountInAccountException as e:
        assert str(e) == "You cannot have negative amounts of money in your account"


def test_catch_account_from_transferring_negative_amount_in_account():
    try:
        account_service.service_transfer_money_between_accounts_by_their_ids(4, 2, -500)
        assert False
    except NegativeWithdrawException as e:
        assert str(e) == "You cannot withdraw negative amounts"


