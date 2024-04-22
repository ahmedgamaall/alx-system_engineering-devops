#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee = argv[1]
    rest_api__user = 'https://jsonplaceholder.typicode.com/users/' + employee
    data_request = requests.get(rest_api__user)

    employee_id = data_request.json().get('username')
    task = rest_api__user + '/todos'
    data_request = requests.get(task)
    tasks = data_request.json()

    with open('{}.csv'.format(employee), 'w') as file:
        for task in tasks:
            completed = task.get('completed')

            title_task = task.get('title')

            file.write('"{}","{}","{}","{}"\n'.format(
                employee, employee_id, completed, title_task))
