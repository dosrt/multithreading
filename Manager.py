from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import os

PORT = 5000
KEY = b"3cnepiuIUE54"

class QueueManager(BaseManager):
    pass

class QueueClient() :
    def __init__(self):
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")
        manager = QueueManager(
            address=(os.environ.get("MANAGER_HOST", "localhost"), PORT), authkey=KEY
        )
        manager.connect()
        self.tasks = manager.get_tasks()
        self.results = manager.get_results()

    def getTask(self):
        return self.tasks

    def getResult(self):
        return self.results

if __name__ == "__main__" : 
    #Définition des queues
    task_queue = Queue()
    result_queue = Queue()

    # Enregistrement des queues avec le gestionnaire
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)

    try:
        QueueManager(address=("", PORT), authkey=KEY).get_server().serve_forever()
    finally:
        print()
        print(
            f"exiting with approximately {task_queue.qsize()} items left in task queue"
            f" and {result_queue.qsize()} items left in result queue."
        )