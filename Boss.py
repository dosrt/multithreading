from Manager import QueueClient
from Task import Task

NB_TASKS = 5 

class Boss:
    def __init__(self):
        self.client = QueueClient()
        #self.num_tasks = num_tasks
        #self.task_queue = self.client.getTask() #certainement pas obligatoire de récupérer le queue

    def add_task(self, task):
        self.client.tasks.put(task)

    def start(self):
        # Ajouter des tâches de test
        for i in range(NB_TASKS):
            task = Task(i, 6000)
            print("Created task number: " + str(task.identifier))
            self.add_task(task)
            print(f"Task {i} added to the task queue.")

if __name__ == '__main__':
    print(f"Il faudra traiter {NB_TASKS} tâches")
    boss = Boss()
    boss.start()