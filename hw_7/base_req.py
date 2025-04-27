import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        response = requests.post(self.url + '/auth/login',json=creds)
        assert response.status_code == 200, "Not expected status code"
        return response.json()["user_token"]

    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active=True):

        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        response = requests.post(self.url + "/employee/create", json=employee_data)
        assert response.status_code == 200, "Not expected status code"
        return response.json()

    def get_employee(self, employee_id):
        response = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert response.status_code == 200 or response.status_code == 404, "Not expected status code"
        return response.json()

    def update_employee(self, employee_id, **kwargs):
        cl_token = self.get_token()
        update_data = {key: value for key, value in kwargs.items() if value is not None}
        response = requests.patch(f"{self.url}/employee/change/1/?client_token={cl_token}", json=update_data)
        assert response.status_code == 200, "Not expected status code"
        return response.json()