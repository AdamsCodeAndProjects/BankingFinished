# API folder
"""
As a customer, I can create a new bank account with a starting balance. (create_account)
As a customer, I can view the balance of a specific account. (get_account_by_id)
As a customer, I can make a withdrawal or deposit to a specific account.
(deposit_into_account_by_id, withdraw_from_account_by_id)
As a customer, I can transfer money between accounts (transfer_money_between_accounts_by_their_ids)
As a customer, I can update my personal information (update_customer_by_id)
As a customer, I can view my personal information (get_customer_by_id)
As a customer, I can close any of my bank accounts (delete_account_by_id)
As a customer, I can end my business relationship with the bank (delete_customer_by_id)
As the system, I reject invalid transactions.
Ex:
A withdrawal that would result in a negative balance.
A deposit or withdrawal of negative money.
"""
from flask import Flask, request, jsonify

from custom_exceptions.AccountExceptions import NegativeWithdrawException, NegativeAmountInAccountException
from custom_exceptions.duplicate_exceptions import DuplicateAccountIDException, DuplicateCustomerIDException
from data_access_layer.implementation_classes.account_dao_implementation import AccountDAOImp
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from data_access_layer.implementation_classes.customer_dao_implementation import CustomerDAOImp
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.accounts import Account
from entities.customers import Customer
from service_layer.implementation_services.account_postgres_service import AccountPostgresService
from service_layer.implementation_services.account_service_imp import AccountServiceImp
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresService
from service_layer.implementation_services.customer_service_imp import CustomerServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)
account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)


@app.route("/customer", methods=["post"])
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["dateOfBirth"],
            customer_data["customerId"]
        )
        customer_to_return = customer_service.service_create_customer_entry(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json

    except DuplicateAccountIDException as e:

        # can either pass a str or a json
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

    # get customer info


@app.get("/customer/<customer_id>")
def get_customer_by_id(customer_id: str):
    result = customer_service.service_get_customer_by_id(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers_information()
    customers_as_dictionary = []
    for customers in customers_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)


@app.patch("/customer/update")
def update_customer():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["dateOfBirth"],
            int(customer_data["customerId"])
        )
        updated_customer = customer_service.service_update_customer_by_id(new_customer)
        return "Customer updated successfully.  The customer info is now " + str(updated_customer)
    except DuplicateCustomerIDException as e:
        return str(e)


@app.delete("/customer/<customer_id>")
def delete_customer_by_id(customer_id: str):
    result = customer_service.service_delete_customer_by_id(int(customer_id))
    if result:
        return "Customer with ID of {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong.  Customer with ID of {} was not deleted".format(customer_id)


@app.post("/account")
def create_account():
    try:
        body = request.get_json()
        new_account = Account(
            body["customerId"],
            body["accountId"],
            body["amountInAccount"]

        )
        newly_created_account = account_service.service_create_account(new_account)
        created_account_as_dictionary = newly_created_account.make_account_dictionary()
        return jsonify(created_account_as_dictionary), 201
    except DuplicateAccountIDException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    account = account_service.service_get_account_by_id(int(account_id))
    account_as_dictionary = account.make_account_dictionary()
    return jsonify(account_as_dictionary), 200


@app.patch("/account/<account_id>")
def deposit_into_account_by_id(account_id: str):
    try:
        account_data = request.get_json()
        new_update = account_data["deposit"]
        returned_account = account_service.service_get_account_by_id(int(account_id))
        updated_account = account_service.service_deposit_into_account_by_id(returned_account.account_id,
                                                                             int(new_update))
        updated_account_as_dictionary = updated_account.make_account_dictionary()
        return jsonify(updated_account_as_dictionary), 200
    except DuplicateAccountIDException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.post("/account/<account_id>")
def withdraw_from_account_by_id(account_id: str):
    try:
        account_data = request.get_json()
        new_update = account_data["withdraw"]
        returned_account = account_service.service_get_account_by_id(int(account_id))
        updated_account = account_service.service_withdraw_from_account_by_id(returned_account.account_id,
                                                                              int(new_update))
        updated_account_as_dictionary = updated_account.make_account_dictionary()
        return jsonify(updated_account_as_dictionary), 200
    except DuplicateAccountIDException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)
    except NegativeWithdrawException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.post("/account/<account_id>/<receiving_id>")
def transfer_money_between_accounts_by_their_ids(account_id: str, receiving_id: str):
    try:
        account_data = request.get_json()
        new_update = account_data["transferAmount"]
        sending_account = account_service.service_get_account_by_id(int(account_id))
        receiving_account = account_service.service_get_account_by_id(int(receiving_id))
        transferring = account_service.service_transfer_money_between_accounts_by_their_ids(sending_account.account_id,
                                                                                            receiving_account.account_id,
                                                                                            new_update)
        my_transfer_list = []
        for transfer in transferring:
            transfer_dict = transfer.make_account_dictionary()
            my_transfer_list.append(transfer_dict)
        return jsonify(my_transfer_list), 200
    except NegativeAmountInAccountException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)
    except NegativeWithdrawException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.get("/accounts/<customer_id>")
def get_all_customer_accounts_by_id(customer_id: str):
    accounts = account_service.service_get_all_customer_accounts_by_id(int(customer_id))
    accounts_as_dictionaries = []
    for acc in accounts:
        account_as_dictionary = acc.make_account_dictionary()
        accounts_as_dictionaries.append(account_as_dictionary)
    return jsonify(accounts_as_dictionaries), 200


@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_accounts()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.make_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


@app.delete("/account/<account_id>")
def delete_account_by_id(account_id: str):
    result = account_service.service_delete_account_by_id(int(account_id))
    if result:
        return "Account ID of {} has been deleted".format(account_id)
    else:
        return "Something went wrong:  Account ID of {} was not deleted".format(account_id)


app.run()
