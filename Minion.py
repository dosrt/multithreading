from Manager import QueueManager
from multiprocessing import Process

class Minion:
    from Manager import QueueManager

class Minion:
    def __init__(self, manager):
        self.manager = manager
        self.task_queue = manager.get_task_queue()
        self.result_queue = manager.get_result_queue()

    def process_task(self, task):
        task.work()
        self.result_queue.put(task)

    def start(self):
        while True:
            if not self.task_queue.empty():
                task = self.task_queue.get()
                self.process_task(task)

if __name__ == '__main__':
    manager = QueueManager(address=('localhost', 5000), authkey=b'password')
    manager.connect()

    minion = Minion(manager)
    minion.start()