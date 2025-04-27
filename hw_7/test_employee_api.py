from base_req import EmployeeApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_create_employee():
    employee = api.create_employee(
        first_name="Alex",
        last_name="Grundstein",
        middle_name="John",
        company_id=3,
        email="alexjohn@emale.com",
        phone="+380441234567",
        birthdate="1986-01-01"
    )
    assert "id" in employee, "Expected key 'id'"
    assert employee["first_name"] == "Alex", "Expected 'first_name' is Alex"
    assert employee["last_name"] == "Grundstein", "Expected 'last_name' is Grundstein"
    assert employee["middle_name"] == "John", "Expected 'middle_name' is John"
    assert employee["company_id"] == 3, "Expected 'company_id' is 3"
    assert employee["email"] == "alexjohn@emale.com", "Expected 'email' is alexjohn@emale.com"
    assert employee["phone"] == "+380441234567", "Expected 'phone' is +380441234567"
    assert employee["birthdate"] == "1986-01-01", "Expected 'birthdate' is 1986-01-01"
    assert employee["is_active"] is True, "Expected - 'is_active' is True"


def test_get_employee_info():
    employee = api.create_employee(
        first_name="John",
        last_name="Smith",
        middle_name="Jameson",
        company_id=2,
        email="jhonsmith@emale.com",
        phone="+380440987654",
        birthdate="1968-10-19"

    )
    employee_id = employee["id"]
    received_employee = api.get_employee(152)
    assert received_employee["id"] == 152, "Expected 'id' is {}".format(received_employee["id"])


def test_update_employee():
    employee = api.create_employee(
        first_name="Fred",
        last_name="Cheep",
        middle_name="Jordan",
        company_id=4,
        email="cheepfred@emale.com",
        phone="+8044678346578",
        birthdate="1996-12-30"

    )
    employee_id = employee["id"]
    updated_employee = api.update_employee(
        employee_id,
        first_name="Updated Fred",
        email="newfred@yahoo.com",
        is_active=False
    )
    assert updated_employee["first_name"] == "Updated Fred", "Expected 'first_name' is Updated Fred"
    assert updated_employee["email"] == "newfred@yahoo.com", "Expected 'email' is newfred@yahoo.com"
    assert updated_employee["is_active"] is False, "Expected - 'is_active' is False"
