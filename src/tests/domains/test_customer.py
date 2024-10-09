from domains.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name='willian', email='willian@email.com')
    print(customer.model_dump)
