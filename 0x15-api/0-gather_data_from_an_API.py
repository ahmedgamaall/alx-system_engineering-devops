#!/usr/bin/python3
"""gather data from API"""

import requests
from sys import argv
import re

rest_api = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            employee_id = int(argv[1])
            requests_data = requests.get('{}/users/{}'.format(
                rest_api, employee_id)).json()
            task_id = requests.get('{}/todos'.format(rest_api)).json()
            employee_name = requests_data.get('name')
            tasks = list(filter(
                lambda x: x.get('userId') == employee_id, task_id))
            completed_list_tasks = list(filter(
                lambda x: x.get('completed'), tasks))
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
