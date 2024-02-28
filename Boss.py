from Manager import QueueClient
from Task import Task

class Boss:
    def __init__(self, num_tasks):
        self.client = QueueClient()
        self.num_tasks = num_tasks
        self.task_queue = self.client.getTask() #certainement pas obligatoire de récupérer le queue

    def add_task(self, task):
        self.client.tasks.put(task)

    def start(self):
        # Ajouter des tâches de test
        for i in range(self.num_tasks):
            task = Task(i, 6000)
            self.add_task(task)
            print(f"Task {i} added to the task queue.")

if __name__ == '__main__':
    task_number = 5 
    print(f"Il faudra traiter {task_number} tâches")
    boss = Boss(task_number)
    boss.start()