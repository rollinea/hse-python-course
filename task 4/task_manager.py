class Task:
    def __init__(self, id_, name, description):
        self._id = id_
        self._name = name
        self._description = description

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

class SubTask(Task):
    def __init__(self, id_, name, description, parent_id):
        super().__init__(id_, name, description)
        self._parent_id = parent_id

    def get_parent_id(self):
        return self._parent_id


class ComplexTask(Task):
    def __init__(self, id_, name, description, subtasks):
        super().__init__(id_, name, description)
        self.subtasks_ids = set(subtasks)

    def get_subtasks_ids(self):
        return self.subtasks_ids


class TaskManager:
    _idGenerator = 0

    def __init__(self):
        self._tasks = {}
        self._subtasks = {}
        self._complex_tasks = {}

    @staticmethod
    def __get_and_increment_id():
        current_id = TaskManager._idGenerator
        TaskManager._idGenerator += 1
        return current_id

    def create_task(self, name, description):
        current_id = TaskManager.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self._tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, parent_id):
        current_id = TaskManager.__get_and_increment_id()
        new_subtask = SubTask(current_id, name, description, parent_id)
        parent = self._complex_tasks[parent_id]
        parent.subtasks_ids.add(current_id)
        self._tasks[current_id] = new_subtask
        self._subtasks[current_id] = new_subtask
        return new_subtask

    def create_complex_task(self, name, description, subtasks):
        parent_id = TaskManager.__get_and_increment_id()
        new_complex_task = ComplexTask(parent_id, name, description, set())
        self._tasks[parent_id] = new_complex_task
        self._complex_tasks[parent_id] = new_complex_task

        for subtask in subtasks:
            self.create_subtask(subtask[0], subtask[1], parent_id)

        return new_complex_task

    def get_tasks(self):
        return self._tasks

    def get_subtasks(self):
        return self._subtasks

    def get_complex_tasks(self):
        return self._complex_tasks

    def get_tasks_by_id(self, id_):
        try:
            task = self._tasks[id_]
            return task
        except:
            print('There is no task with this id!')
            return None

    def get_subtasks_by_id(self, id_):
        try:
            task = self._subtasks[id_]
            return task
        except:
            print('There is no task with this id!')
            return None

    def get_complex_tasks_by_id(self, id_):
        try:
            task = self._complex_tasks[id_]
            return task
        except:
            print('There is no task with this id!')
            return None

    def remove_tasks(self):
        self._tasks = {}
        self._subtasks = {}
        self._complex_tasks = {}

    def remove_subtasks(self):
        keys = list(self._subtasks.keys())
        for task_id in keys:
            self.remove_subtask_by_id(task_id)

    def remove_complex_tasks(self):
        keys = list(self._complex_tasks.keys())
        for task_id in keys:
            self.remove_complex_task_by_id(task_id)

    def remove_task_by_id(self, id_):
        self._tasks.pop(id_)
        try:
            self._subtasks.pop(id_)
            self._complex_tasks.pop(id_)
        except:
            pass

    def remove_subtask_by_id(self, id_):
        parent_id = self._subtasks[id_]._parent_id
        self._subtasks.pop(id_)
        self._tasks.pop(id_)
        self._complex_tasks[parent_id].subtasks_ids.remove(id_)

        if not self._complex_tasks[parent_id].subtasks_ids:
            self._tasks.pop(parent_id)
            self._complex_tasks.pop(parent_id)

    def remove_complex_task_by_id(self, id_):
        current_task = self._complex_tasks[id_]
        ids = list(current_task.subtasks_ids)
        for subtask_id in ids:
            self.remove_subtask_by_id(subtask_id)