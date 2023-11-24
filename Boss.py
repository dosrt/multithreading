from Manager import QueueManager
from multiprocessing import Process
from Task import Task

class Boss:
    def __init__(self, manager):
        self.manager = manager
        self.task_queue = manager.get_task_queue()

    def add_task(self, task):
        self.task_queue.put(task)

    def start(self):
        # Ajouter des tâches de test
        for i in range(5):
            task = Task(i, 6000)
            self.add_task(task)
            print(f"Task {i} added to the task queue.")

if __name__ == '__main__':
    manager = QueueManager(address=('localhost', 5000), authkey=b'password')
    manager.start()

    boss = Boss(manager)
    boss.start()