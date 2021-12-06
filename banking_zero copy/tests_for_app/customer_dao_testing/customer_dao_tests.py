import pytest
# from data_access_layer.implementation_classes.customer_dao_implementation import CustomerDAOImp
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer

customer_dao_postgres = CustomerPostgresDAO()
# customer_dao_implementation = CustomerDAOImp()
customer = Customer("Test", "Customer", 120199, 8)
#                                  FN,       LN,          DOB, CUST ID, ACCT ID
customer_for_postgres = Customer("Alexander", "Hamilton", 17200732, 0)

random_names = {"Bob"}
random_names.add("Sally")
random_names.add("Bill")
random_names.add("Timmy")

random_names = random_names.pop()


def test_create_customer_entry_success():
    new_customer: Customer = customer_dao_postgres.create_customer_entry(customer_for_postgres)
    print(new_customer.customer_id)
    assert new_customer.customer_id != 0


def test_get_customer_by_id_success():
    returned_customer: Customer = customer_dao_postgres.get_customer_by_id(1)
    assert returned_customer.customer_id != 0


def test_get_all_customers_information_success():
    customer_list = customer_dao_postgres.get_all_customers_information()
    assert len(customer_list) >= 2


def test_update_customer_by_id_success():
    update_info = Customer("John", "Doe", 110194, 2)
    updated_customer: Customer = customer_dao_postgres.update_customer_by_id(update_info)
    assert updated_customer.customer_id == update_info.customer_id


def test_delete_customer_by_id_success():
    confirm_customer_deleted = customer_dao_postgres.delete_customer_by_id(3)
    assert confirm_customer_deleted


