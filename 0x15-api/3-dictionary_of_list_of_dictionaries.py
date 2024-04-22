#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests

if __name__ == '__main__':
    rest_api = "https://jsonplaceholder.typicode.com/users"

    requests_data = requests.get(rest_api)
    employees = requests_data.json()

    employee_dict = {}
    for employee in employees:
        employee_id = employee.get('id')
        employee_username = employee.get('username')
        rest_api = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
        rest_api = rest_api + '/todos/'
        requests_data = requests.get(rest_api)

        tasks = requests_data.json()
        employee_dict[employee_id] = []
        for task in tasks:
            completed_tasks = task.get('completed')
            employee_task = task.get('title')
            employee_dict[employee_id].append({
                "task": employee_task,
                "completed": completed_tasks,
                "username": employee_username
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(employee_dict, f)
