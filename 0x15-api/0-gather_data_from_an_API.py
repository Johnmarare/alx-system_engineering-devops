#!/usr/bin/python3
"""
Gather data from an api
"""
from sys import argv
import requests

if __name__ == '__main__':
    emp_id = argv[1]
    burl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(emp_id)

    s = requests.Session()

    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = s.get(url)
    name = response.json()['name']

    response = s.get(burl)
    body = response.json()
    tasks_done = []
    for b in body:
        if b.get('completed', False):
            tasks_done.append('\t' + b['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(tasks_done), len(body)))
    print(*tasks_done, sep='\n')
