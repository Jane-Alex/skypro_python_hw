import requests
import json
base_url = "https://x-clients-be.onrender.com"
  
class Employer:
    def __init__(self, url=base_url):
        self.url = url

    # получить список сотрудников для компании
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(self.url + '/employee/', params=company)
        return response.json()
    
    # добавить нового сотрудника
    def add_new(self, token: str, body: json):
        headers = {'x-client-token' : token}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        return response.json()
    
    # получить сотрудника по id
    def get_info(self, employee_id: int):
        response = requests.get(self.url + '/employee/' + str(employee_id))
        return response
    
    # изменить иноформацию о сотруднике
    def change_info(self, token: str, employee_id: int, body:json):
        headers = {'x-client-token' : token}
        response = requests.patch(self.url + '/employee/' + str(employee_id), headers=headers, json=body)
        return response
