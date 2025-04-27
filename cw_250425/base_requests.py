import requests



class CompanyApi:

    def __init__(self, url):
        self.url = url


    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        response = requests.post(self.url + '/auth/login',json=creds)
        assert response.status_code == 200, "Not expected status code"
        return response.json()["user_token"]

    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
            }
        response = requests.post(self.url + '/company/create',json=company)
        assert response.status_code == 201, "Not expected status code"
        return response.json()

    def get_company(self, company_id):
        response = requests.get(f"{self.url}/company/{company_id}")
        assert response.status_code == 200 or response.status_code == 404, "Not expected status code"
        return response.json()

    def edit_company(self, company_id, new_name, new_description):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{company_id}?client_token={client_token}"
        company = {
            "name": new_name,
            "description": new_description
        }
        response = requests.patch(url_with_token, json=company)
        assert response.status_code == 200, "Not expected status code"

    def delete_company(self, company_id):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/{company_id}?client_token={client_token}"
        response = requests.delete(url_with_token)
        assert response.status_code == 200, "Not expected status code"

    def get_company_list(self):
        response = requests.get(f"{self.url}/company")
        assert response.status_code == 200, "Not expected status code"


