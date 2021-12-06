from custom_exceptions.duplicate_exceptions import DuplicateCustomerIDException
from data_access_layer.implementation_classes.customer_dao_implementation import CustomerDAOImp
from entities.customers import Customer
from service_layer.implementation_services.customer_service_imp import CustomerServiceImp

# Sad path testing

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer("service", "testing", 100, 5, 15)
customer_update = Customer("update", "test", 101, 2, 1)


def test_validate_create_customer_method():
    try:
        unexpected_customer = customer_service.service_create_customer_entry(customer)
        # for existing_customer in customer_service.customer_dao.customer_list:
        # customer_service.service_create_customer_entry(customer)
        # this test will now fail if line above is not working like intended
        assert False
    except DuplicateCustomerIDException as e:
        assert str(e) == "Customer ID is taken by another!"

# def test_validate_update_customer_method():
#     try:
#         customer_service.service_update_customer_by_id(customer_update.customer_id)
#         assert False
#     except DuplicateCustomerIDException as e:
#         assert str(e) == "Customer ID is taken by another!"
