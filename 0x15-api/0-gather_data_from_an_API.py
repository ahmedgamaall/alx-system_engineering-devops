#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except Exception as a:
        exit()

    rest_api = 'https://jsonplaceholder.typicode.com'

    one_employee = requests.get('{}/users/{}'.format(
        rest_api, employee_id)).json()
    if one_employee == {}:
        exit()

    employee_name = one_employee.get('name')

    tasks = requests.get('{}/todos'.format(rest_api)).json()

    tasks_counter = 0
    tasks_done_counter = 0
    todo_tasks = []
    for task in tasks:
        if task.get('userId') == employee_id:
            tasks_counter += 1
            if task.get('completed'):
                tasks_done_counter += 1
                todo_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, tasks_done_counter, tasks_counter))
    for task in todo_tasks:
        print("\t {}".format(task))
