#!/usr/bin/python3
"""gather data from API"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except Exception as error:
        exit()

    rest_api = 'https://jsonplaceholder.typicode.com'

    employee_data = requests.get(f'{rest_api}/users/{employee_id}').json()
    if employee_data == {}:
        exit()
    employee_name = employee_data.get('name')

    tasks = requests.get(f'{rest_api}/todos').json()

    tasks_number = 0
    tasks_number_done = 0
    todo_tasks_list = []
    for task in tasks:
        if task.get('userId') == employee_id:
            tasks_number += 1
            if task.get('completed'):
                tasks_number_done += 1
                todo_tasks_list.append(task.get('title'))

    print(f"Employee {employee_name} is done with tasks({tasks_number_done}/{tasks_number}):")
    for task in todo_tasks_list:
        print(f"\t {task}")
