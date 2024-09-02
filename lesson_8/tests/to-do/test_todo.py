import pytest
from lesson_8.pages.TodoMain import Task

todo_page = Task()

def test_todo():
    # получение списка задач
    response = todo_page.get_list()
    assert response.status_code == 200

    # создание новой
    params = {'title': 'New Task', 'completed': 'false'}
    task_id = todo_page.create(params)
    assert task_id is not None

    # переименование задачи
    params = {'title': 'Renamed Task'}
    rename_task = todo_page.rename(task_id, params)
    assert rename_task.json()['title'] == 'Renamed Task'

    # информация о созданной задаче
    info = todo_page.info(task_id)
    assert info.json()['title'] == 'Renamed Task'
    assert info.json()['id'] == task_id

    # отметка о выполнении
    params = {'completed': 'true'}
    status_true = todo_page.change_status(task_id, params)
    assert status_true.status_code == 200
    assert status_true.json()['completed'] == True 

    # снятие отметки о выполнении
    params = {'completed': 'false'}
    status_false = todo_page.change_status(task_id, params)
    assert status_false.status_code == 200
    assert status_false.json()['completed'] == False

    # удаление задачи
    delete = todo_page.delete(task_id)
    assert delete == 200
