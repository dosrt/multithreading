from Manager import QueueManager
from Boss import Boss
from Minion import Minion
from multiprocessing import Process

def main():
    manager = QueueManager(address=('', 5000), authkey=b'password')
    manager.start()

    boss = Boss(manager)
    minion = Minion(manager)

    boss_process = Process(target=boss.start)
    minion_process = Process(target=minion.start)

    boss_process.start()
    minion_process.start()

    boss_process.join()
    minion_process.join()

if __name__ == '__main__':
    main()