#!/usr/bin/python3
# This script retrieves and displays the TODO list progress of a given employee based on the employee ID

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data. Please try again.")
        return

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    employee_name = employee_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task["title"] for task in todos_data if task["completed"]]

    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    print(f"{employee_name}: {len(done_tasks)} completed tasks out of {total_tasks} total tasks")

    for task in done_tasks:
        print(f"\t{task}")

employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)
