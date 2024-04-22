#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format."""

import json
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
    username_employee = one_employee.get('username')

    tasks = requests.get('{}/todos'.format(rest_api)).json()

    employee_tasks = []
    employee_task_dict = {}

    for task in tasks:
        if task.get('userId') == employee_id:
            employee_tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username_employee,
            })
    employee_task_dict["{}".format(employee_id)] = employee_tasks
    with open("{}.json".format(employee_id), "w") as file:
        json.dump(employee_task_dict, file)
