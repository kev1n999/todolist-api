# 📝 TodoList API

A simple Todo List API to create and manage tasks.

---

## Features

* Create tasks
* Fetch all tasks
* Update tasks
* Delete tasks

---

## How to use
1. Clone the repository
```
git clone https://github.com/kev1n999/todolist-api/
```
2. Access the project root
```
cd todolist-api 
``` 
3. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
4. Install the requirements
```
pip3 install -r requirements.txt
```
5. Create an .env
```.env
MONGO_URI=your mongodb uri
SERVER_PORT=8000
```
6. Run api
```
python3 -m src.main
```

---

## Task Structure

```json
{
  "name": "Task name",
  "description": "Task description",
  "priority": "low",
  "status": "created"
}
```

---

## Routes

### POST `/create-task`
Create a new task.

### GET `/fetch-tasks`
Fetch all tasks.
If you want to get a specif task, use a url parameter to filter(You can filter by name, status or priority)

Example by task name:
```
/find-tasks?filter=name&filter_content=Study
```

### PATCH `/update-task` 
Update datas or fields of an existing task.

Exemple by status:
```
"/update-task?filter=status&filter_content=pending&status=completed"
```

### DELETE `/delete-task`
Delete a task

Example by task priority:
```
/delete-task?filter=priority&filter_content=low 
```
