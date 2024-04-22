#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format."""

import csv
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
    for task in tasks:
        if task.get('userId') == employee_id:
            employee_tasks.append(task)

    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        file_writer = csv.file_writer(file, quoting=csv.QUOTE_NONNUMERIC)

        for task in employee_tasks:
            file_writer.writerow([
                "{}".format(employee_id), "{}".format(username_employee),
                "{}".format(task.get('completed')),
                "{}".format(task.get('title'))])
