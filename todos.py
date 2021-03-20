class TaskManager:
    def __init__(self):
        self.tasks = []


    def parse(self, command):
        return Action("add", command[2:])


    def parse2(self, command):
        return Delete("delete", command[2:])



class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Delete:
    def __del__(self, name2, description2):
        self.name2 = name2
        self.description2 = description2