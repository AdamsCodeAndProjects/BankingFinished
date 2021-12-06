from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer

customer_dao = CustomerPostgresDAO()
customer: Customer = Customer("first", "last", 10101999, 4)

random_names = {"Bert"}
random_names.add("Ernie")
random_names.add("Genghis")
random_names.add("Alexander")

random_name = random_names.pop()
update_customer = Customer(random_name, "customer", 19990201, 5)


customer_to_delete = Customer(random_names.pop(), random_names.pop(), 10101998, 7)


def test_create_customer_entry_success():
    created_customer = customer_dao.create_customer_entry(customer)
    assert created_customer.customer_id != 0


def test_get_customer_by_id_success():
    george_washington = customer_dao.get_customer_by_id(1)
    assert george_washington.first_name == "George" and george_washington.last_name == "Washington"


def test_get_all_customers_information_success():
    customers = customer_dao.get_all_customers_information()
    assert len(customers) > 2


def test_update_customer_by_id_success():
    updated_customer = customer_dao.update_customer_by_id(update_customer)
    assert updated_customer.first_name == random_name


def test_delete_customer_by_id_success():
    customer_to_be_deleted = customer_dao.create_customer_entry(customer_to_delete)
    result = customer_dao.delete_customer_by_id(customer_to_be_deleted.customer_id)
    assert result
