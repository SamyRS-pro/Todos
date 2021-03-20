from todos import TaskManager, Action, Delete


def test_can_create_an_action():
    action = Action("add", "first task")
    assert action.name == "add"
    assert action.description == "first task"

def test_can_delete_an_action():
    action2 = Delete("delete", "second task")
    assert action2.name2 == "delete"
    assert action2.description2 == "second task"


def test_can_create_a_task_manager():
    task_manager = TaskManager()


def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []




def test_parse_add():
    command = "+ first task"
    task_manager = TaskManager()

    action = task_manager.parse(command)

    assert action.name == "add"
    assert action.description == "first task"


def test_parse_delete():
    command2 = "- second task"
    task_manager = TaskManager()

    action2 = task_manager.parse2(command2)

    assert action2.name2 == "delete"
    assert action2.description2 == "second task"

