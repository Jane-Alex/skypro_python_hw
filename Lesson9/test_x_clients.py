import pytest
from EmployeeApi import Employer
from DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

#получаем список сотрудников из БД и API, сравниваем их
def test_get_list_of_employers():  
    db.create_company('Name_company', 'Nice') #создаем компанию
    max_id = db.last_company_id() #получаем id последней созданной компании
    print(max_id)
    db.create_employer(max_id, "Mary", "Li", 89165553355) #добавляем сотрудника в компанию
    #получаем список сотрудников из последней созданной компании БД/API
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list) #сравниваем
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id) #удаляем сотрудника
    db.delete(max_id) #удаляем последнуюю созданную компанию

# Сравниваем инфо о сотруднике полученную по API с БД
def test_assertion_data():
    db.create_company('Name_company_2', 'Good')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Mary", "Li", 89165553355)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Mary"
    assert get_api_info["lastName"] == "Li"
    assert get_api_info["phone"] == "89165553355"
    db.delete_employer(employer_id) #удаляем сотрудника
    db.delete(max_id) #удаляем компанию

def test_add_new_employer():
    db.create_company('Name_company_3', 'Nice') #создаем компанию
    max_id = db.last_company_id() #получаем id последней созданной компании
    db.create_employer(max_id, "Mary", "Li", 89165553355)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    assert response["companyId"] == max_id
    assert response["firstName"] == "Mary"
    assert response["isActive"] == True
    #assert response["LastName"] == "Li"
    db.delete_employer(employer_id)
    db.delete(max_id)

def test_update_user_info():
    db.create_company('Name_company_4', 'Nice')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Mary", "Li", 89165553355)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Jack", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Jack"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)

