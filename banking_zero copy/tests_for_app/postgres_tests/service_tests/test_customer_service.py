from custom_exceptions.duplicate_exceptions import DuplicateCustomerIDException, NoIdFoundException
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

customer_with_duplicate_id = Customer("first", "last", 20001020, 4)


def test_catch_duplicate_customer_id_for_create_method():
    try:
        customer_service.service_create_customer_entry(customer_with_duplicate_id)
        assert False
    except DuplicateCustomerIDException as e:
        assert str(e) == "Customer ID taken by another"


def test_catch_duplicate_customer_id_for_update_method():
    try:
        customer_service.service_update_customer_by_id(customer_with_duplicate_id)
        assert True
    except DuplicateCustomerIDException as e:
        assert str(e) == "Customer ID taken by another"

