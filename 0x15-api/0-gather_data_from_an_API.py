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
            employee_id = int(argv[1])
            data_request = requests.get('{}/users/{}'.format(rest_api, employee_id)).json()
            tasks_request = requests.get('{}/todos'.format(rest_api)).json()
            employee_name = data_request.get('name')
            tasks = list(filter(lambda t: t.get('userId') == employee_id, tasks_request))
            completed_list_tasks = list(filter(lambda a: a.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(completed_list_tasks),
                    len(tasks)
                )
            )
            if len(completed_list_tasks) > 0:
                for task in completed_list_tasks:
                    print('\t {}'.format(task.get('title')))
