from custom_exceptions.duplicate_exceptions import DuplicateAccountIDException
from data_access_layer.implementation_classes.account_dao_implementation import AccountDAOImp
from entities.accounts import Account
from service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

bad_account_number = Account(5, 50000, 0)
bad_update_account = Account(5, 5, 0)

# Sad Path Testing(Fails in a way that we intend for it to fail)


def test_catch_creating_account_with_duplicate_id():
    try:
        account_service.service_create_account(bad_account_number)
        assert False
    except DuplicateAccountIDException as e:
        assert str(e) == "You cannot have duplicate account IDs"


# def test_catch_updating_team_with_duplicate_id():
#     try:
#         pass   # account_service.service_update_account_by_id(bad_update_account)
#     # assert False
#     except DuplicateAccountIDException as e:
#         assert str(e) == "You cannot have duplicate account IDs"


