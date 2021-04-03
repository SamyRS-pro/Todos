from todos import TaskManager, Action, Delete, Make, Do


def test_can_create_an_action():
    action = Action("add", "first task")
    assert action.name == "add"
    assert action.description == "first task"
    assert action.number == 1


def test_can_delete_an_action():
    action2 = Delete("delete", "second task",1)
    assert action2.name2 == "delete"
    assert action2.description2 == "second task"
    assert action2.number2 == 1

def test_can_make_an_action():
    action3 = Make("make", "third task",1)
    assert action3.name3 == "make"
    assert action3.description3 == "third task"
    assert action3.number3 == 1

def test_can_do_an_action():
    action4 = Do("do", "fourth task",1)
    assert action4.name4 == "do"
    assert action4.description4 == "fourth task"
    assert action4.number4 == 1


def test_can_create_a_task_manager():
    task_manager = TaskManager()


def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []



def test_parse_add():
    command = "+ first task"
    task_manager = TaskManager()

    action = task_manager.parse_add(command)

    assert action.name == "add"
    assert action.description == "first task"
    assert action.number == 1


def test_parse_delete():
    command2 = "- second task"
    task_manager = TaskManager()

    action2 = task_manager.parse_delete(command2)

    assert action2.name2 == "delete"
    assert action2.description2 == "second task"
    assert action2.number2 == 1

def test_parse_make():
    command3 = "x third task"
    task_manager = TaskManager()

    action3 = task_manager.parse_make(command3)

    assert action3.name3 == "make"
    assert action3.description3 == "third task"
    assert action3.number3 == 1

def test_parse_Do():
    command4 = "o fourth task"
    task_manager = TaskManager()

    action4 = task_manager.parse_do(command4)

    assert action4.name4 == "do"
    assert action4.description4 == "fourth task"






