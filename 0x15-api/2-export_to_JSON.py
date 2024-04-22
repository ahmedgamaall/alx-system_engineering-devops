#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except Exception as a:
        exit()

    rest_api = 'https://jsonplaceholder.typicode.com'
    employee_data = requests.get(f'{rest_api}/users/{employee_id}').json()
    if employee_data == {}:
        exit()
    employee_username = employee_data.get('username')

    tasks_list = requests.get(f'{rest_api}/todos').json()

    employee_tasks_list = []
    employee_user_task = {}

    for task in tasks_list:
        if task.get('userId') == employee_id:
            employee_tasks_list.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_username,
            })
    employee_user_task[f"{employee_id}"] = employee_tasks_list
    with open(f"{employee_id}.json", "w") as outfile:
        json.dump(employee_user_task, outfile)
