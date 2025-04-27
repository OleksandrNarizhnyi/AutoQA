from base_requests import CompanyApi

base_url = "http://5.101.50.27:8000"

def test_create_company():
    api = CompanyApi(base_url)

    companies_before = api.get_company_list()
    initial_count = len(companies_before)
    api.create_company(name="Name", description="Description")
    companies_after = api.get_company_list()
    assert len(companies_after) == initial_count + 1

def test_get_one_company():
    api = CompanyApi(base_url)

    res = api.create_company(name="Name_id", description="Description_id")
    company_id = res["id"]
    company_by_id = api.get_company(company_id)

    assert company_by_id['name'] == "Name_id"
    assert company_by_id['description'] == "Description_id"
    assert company_by_id['is_active'] is True

def test_delete_company():
    api = CompanyApi(base_url)
    name = "Company to be deleted"
    descr = "Delete me"
    res = api.create_company(name, descr)
    company_id = res["id"]

    api.delete_company(company_id)
    deleted_company = api.get_company(company_id)
    assert deleted_company['detail'] == "Компания не найдена"

