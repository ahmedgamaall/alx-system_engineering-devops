#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests


if __name__ == "__main__":

    rest_api = 'https://jsonplaceholder.typicode.com'

    users_list = requests.get('{}/users'.format(rest_api)).json()

    tasks = requests.get('{}/todos'.format(rest_api)).json()
    todos_employees = {}
    for user in users_list:
        user_id = user.get('employee_id')
        employee_tasks = []
        for task in tasks:
            if task.get('userId') == user_id:
                employee_tasks.append({
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })

        todos_employees[user_id] = employee_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(todos_employees, file)
