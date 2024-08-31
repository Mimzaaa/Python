from lesson_8.pages.todoMain import Task


def test_get_list(todo_page: Task):
    tasks = todo_page.get_list()
    assert isinstance(tasks, list)

def test_create_task(todo_page: Task):
    new_task = {"name": "New Task", "completed": False}
    task = todo_page.create(new_task)
    assert task["name"] == new_task["name"]

def test_rename_task(todo_page: Task):
    new_task = {"name": "Task to Rename", "completed": False}
    task = todo_page.create(new_task)
    task_id = task["id"]
    renamed_task = todo_page.rename(task_id, "Renamed Task")
    assert renamed_task["name"] == "Renamed Task"

def test_change_task_status(todo_page: Task):
    new_task = {"name": "Task to Change Status", "completed": False}
    task = todo_page.create(new_task)
    task_id = task["id"]
    updated_task = todo_page.change_status(task_id, True)
    assert updated_task["completed"] == True

def test_delete_task(todo_page: Task):
    new_task = {"name": "Task to Delete", "completed": False}
    task = todo_page.create(new_task)
    task_id = task["id"]
    status_code = todo_page.delete(task_id)
    assert status_code == 204
