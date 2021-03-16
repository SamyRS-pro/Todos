class TaskManager:
    def init(self):
        self.tasks = []


    def parse(self, command):
        return Action("add", command[2:])



class Action:
    def init(self, name, description):
        self.name = name
        self.description = description