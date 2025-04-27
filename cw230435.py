# http://5.101.50.27:8000/company/list

import requests

base_url = "http://5.101.50.27:8000"

def test_get_active_companies():
    response = requests.get(f"{base_url}/company/list")
    assert response.status_code == 200
    companies = response.json()
    active_companies = [company for company in companies if company["is_active"]] # Фильтруем только активные компании
    assert len(active_companies) >= 3, f"Ожидалось >=3 активных компаний, но найдено {len(active_companies)}" # Проверяем, что активных компаний не меньше 3
    print(f"Тест пройден! Найдено {len(active_companies)}  активных компаний.")

def test_auth():
     user_data = {
     'username': 'harrypotter',
     'password': 'expelliarmus'
     }
     response = requests.post(base_url + '/auth/login', json=user_data)
     assert response.status_code == 200
     assert response.json()["user_token"] is not None

# def test_create_company():
#     company = {
#         "name": "My first company",
#         "description": "IT company"
#     }
#     response = requests.post(f"{base_url}/company/create", json=company)
#     assert response.status_code == 201

def test_create_company_empty_body():
     resp = requests.post(base_url + '/company/create', json={})
     response = resp.json()
     assert resp.status_code == 422, f"Ожидался 422, получен {resp.status_code}"
     assert response["detail"][0]["msg"] == "Field required"

def test_create_company_increases_count():
    """Тест: создание компании увеличивает список компаний на 1"""
    # 1. Получаем текущий список компаний
    resp = requests.get(base_url + "/company/list")
    assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
    companies_before = resp.json()  # Преобразуем ответ в JSON
    initial_count = len(companies_before)  # Запоминаем количество компаний до создания новой
    # 2. Создаём новую компанию
    new_company = {
        "name": "Test Company",
        "description": "Automated test creation"
    }
    resp_create = requests.post(base_url + "/company/create", json=new_company)
    assert resp_create.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp_create.status_code}"
    # 3. Повторно получаем список компаний
    resp_after = requests.get(base_url + "/company/list")
    assert resp_after.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp_after.status_code}"
    companies_after = resp_after.json()  # Преобразуем ответ в JSON
    final_count = len(companies_after)  # Запоминаем количество компаний после создания новой
    # 4. Проверяем, что длина списка увеличилась на 1
    assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1} компаний, найдено {final_count}"
    print(f"Тест пройден: до {initial_count}, после {final_count} (добавлена 1 компания).")



