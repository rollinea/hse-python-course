import unittest
from task_manager import TaskManager

'''
Tests on methods:
1. create task
2. create complex task
3. create subtask
4. get tasks
5. get subtasks
6. get complex tasks
7. get task by id
8. remove tasks
9. remove subtasks
10. remove complex tasks
11. remove task by id
12. remove subtask by id
13. remove complex task by id
'''


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_create_task(self):
        name = 'Buy products'
        description = 'Go to the nearest store'
        task = self.manager.create_task(name, description)

        self.assertEqual(task.get_name(), name)
        self.assertEqual(task.get_description(), description)

    def test_create_subtask(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)
        parent_id = complex_task.get_id()

        subtask_name = 'Make a salad'
        subtask_description = 'Fruit salad with apples and oranges'
        subtask = self.manager.create_subtask(subtask_name, subtask_description, parent_id)

        self.assertEqual(subtask.get_name(), subtask_name)
        self.assertEqual(subtask.get_description(), subtask_description)
        self.assertEqual(subtask.get_parent_id(), parent_id)

    def test_create_complex_task(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)
        self.assertEqual(complex_task.get_name(), complex_name)
        self.assertEqual(complex_task.get_description(), complex_description)
        self.assertEqual(len(complex_task.get_subtasks_ids()), len(subtasks))

    def test_get_tasks(self):
        name = 'Buy products'
        description = 'Go to the nearest store'
        task = self.manager.create_task(name, description)
        task_id = task.get_id()

        result = self.manager.get_tasks()

        self.assertEqual(result[task_id], task)
        self.assertTrue(len(result), 1)

    def test_get_subtasks(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)
        parent_id = complex_task.get_id()

        subtask_name = 'Make a salad'
        subtask_description = 'Fruit salad with apples and oranges'
        subtask = self.manager.create_subtask(subtask_name, subtask_description, parent_id)
        subtask_id = subtask.get_id()

        result = self.manager.get_subtasks()

        self.assertTrue(len(result) == 2)
        self.assertEqual(result[subtask_id], subtask)

    def test_get_complex_tasks(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)

        result = self.manager.get_complex_tasks()

        self.assertTrue(len(result) == 1)
        self.assertEqual(result[complex_task.get_id()], complex_task)

    def test_get_tasks_by_id(self):
        name = 'Buy products'
        description = 'Go to the nearest store'
        task = self.manager.create_task(name, description)
        task_id = task.get_id()

        result = self.manager.get_tasks_by_id(task_id)
        self.assertEqual(result, task)

        result = self.manager.get_tasks_by_id(100500)
        self.assertEqual(result, None)

    def test_get_subtasks_by_id(self):
        result = self.manager.get_subtasks_by_id(100500)
        self.assertEqual(result, None)

    def test_get_complex_tasks_by_id(self):
        result = self.manager.get_complex_tasks_by_id(100500)
        self.assertEqual(result, None)

    def test_remove_tasks(self):
        name = 'Buy products'
        description = 'Go to the nearest store'
        task = self.manager.create_task(name, description)

        self.manager.remove_tasks()
        self.assertEqual(self.manager.get_tasks(), {})

    def test_remove_subtasks(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        self.manager.create_complex_task(complex_name, complex_description, subtasks)
        self.manager.remove_subtasks()

        self.assertEqual(self.manager.get_subtasks(), {})
        self.assertEqual(self.manager.get_complex_tasks(), {})

    def test_remove_complex_tasks(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        self.manager.create_complex_task(complex_name, complex_description, subtasks)

        self.manager.remove_complex_tasks()
        self.assertEqual(self.manager.get_complex_tasks(), {})

    def test_remove_task_by_id(self):
        name = 'Buy products'
        description = 'Go to the nearest store'
        task = self.manager.create_task(name, description)

        task_id = task.get_id()
        self.manager.remove_task_by_id(task_id)
        self.assertEqual(self.manager.get_tasks_by_id(task_id), None)

    def test_remove_subtask_by_id(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)
        parent_id = complex_task.get_id()
        subtask_name = 'Make a salad'
        subtask_description = 'Fruit salad with apples and oranges'
        subtask = self.manager.create_subtask(subtask_name, subtask_description, parent_id)
        subtask_id = subtask.get_id()

        self.manager.remove_subtask_by_id(subtask_id)
        self.assertEqual(self.manager.get_tasks_by_id(subtask_id), None)

    def test_remove_complex_task_by_id(self):
        complex_name = 'Cook dinner'
        complex_description = 'Christmas evening with the family'
        subtasks = [['Buy products', 'Go to the nearest store']]
        complex_task = self.manager.create_complex_task(complex_name, complex_description, subtasks)
        task_id = complex_task.get_id()
        subtask_id = complex_task.get_subtasks_ids()

        self.manager.remove_complex_task_by_id(task_id)
        self.assertEqual(self.manager.get_complex_tasks_by_id(task_id), None)
        self.assertEqual(self.manager.get_subtasks_by_id(subtask_id), None)