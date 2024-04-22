#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import re
import requests
from sys import argv

rest_api = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            id = int(argv[1])
            data_requests = requests.get('{}/users/{}'.format(rest_api, id)).json()
            task_requests = requests.get('{}/todos'.format(rest_api)).json()
            employee_name = data_requests.get('name')
            employee_tasks = list(filter(lambda x: x.get('userId') == id, task_requests))
            completed_tasks = list(filter(lambda x: x.get('completed'), employee_tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(completed_tasks),
                    len(employee_tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
