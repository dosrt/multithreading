#!/usr/bin/env python3

import multiprocessing
import os
from multiprocessing.managers import BaseManager

PORT = 5000
KEY = b"3cnepiuIUE54"

class QueueManager(BaseManager):
    pass


class QueueClient:
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


if __name__ == "__main__":
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    QueueManager.register("get_tasks", callable=lambda: task_queue)
    QueueManager.register("get_results", callable=lambda: result_queue)
    try:
        QueueManager(address=("", PORT), authkey=KEY).get_server().serve_forever()
    finally:
        print()
        print(
            f"exiting with approximately {task_queue.qsize()} items left in task queue"
            f" and {result_queue.qsize()} items left in result queue."
        )