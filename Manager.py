from multiprocessing.managers import BaseManager

class QueueClient() : 
    
    pass 

from multiprocessing import Queue

class QueueManager(BaseManager):
    pass

# Définition des queues
task_queue = Queue()
result_queue = Queue()

# Enregistrement des queues avec le gestionnaire
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

