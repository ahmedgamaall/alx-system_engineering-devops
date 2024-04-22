#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
from sys import argv

if __name__ == '__main__':

    rest_api = "https://jsonplaceholder.typicode.com/"

    employee_id = argv[1]

    data_response = requests.get(rest_api + "users/{}".format(employee_id))

    employee = data_response.json()

    employee_params = {"userId": employee_id}

    todos_response = requests.get(rest_api + "todos", params=employee_params)

    todos_list = todos_response.json()

    completed_tasks = []

    for todo in todos_list:
        if todo.get("completed") is True:
            completed_tasks.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}))".format(
        employee.get("name"), len(completed_tasks), len(todos_list)))

    for complete in completed_tasks:
        print("/t {}".format(complete))
