from Manager import QueueClient
from multiprocessing import Process

class Minion:
    from Manager import QueueManager

class Minion:
    def __init__(self):
        self.client = QueueClient()

    def process_task(self, task):
        task.work()
        self.result_queue.put(task)

    def start(self):
        while True:
            if not self.task_queue.empty():
                task = self.task_queue.get()
                self.process_task(task)

if __name__ == '__main__':
    minion = Minion()
    minion.start()