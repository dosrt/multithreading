###### minion #####
from Manager import QueueClient
from multiprocessing import Process
import time

class Minion:
    from Manager import QueueManager

class Minion:
    def __init__(self):
        self.queue = QueueClient()
        self.currentTask = None

    def process_task(self, task):
        task.work()
        self.result_queue.put(task)

    def waitTask(self) : 
        queue = self.queue.getTask()
        task = queue.get()
        if task:
            self.currentTask = task
            return True
        return False
    
    def work(self):
        while True:# Le minion reste toujour en attente de tâches 
            if self.waitTask():
                print ("Début tâche : ", self.currentTask.identifier)
                self.currentTask.work()
                self.queue.results.put(
                (self.currentTask.identifier, self.currentTask.x, self.currentTask.time))
                print ("Fin tâche : ", self.currentTask.identifier)
                self.currentTask = None
            else : 
                print("Queue vide pour le moment")
                time.sleep(5)

if __name__ == '__main__':
    minion = Minion()
    minion.work()