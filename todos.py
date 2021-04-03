class TaskManager:
    def __init__(self):
        self.tasks = []


    def parse_add(self, command):
        return Action("add", command[2:])


    def parse_delete(self, command):
        return Delete("delete", command[2:])

    def parse_make(self, command):
        return Action("make", command[2:])


    def parse_do(self, command):
        return Delete("do", command[2:])



class Action:
    def __init__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number

class Delete:
    def __del__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number

class Make:
    def __del__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number

class Do:
    def __del__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number