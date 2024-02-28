##### TASK ####
import numpy as np 
from time import perf_counter
import json
# recupérer sur parallel-101

class Task : 
    
    def __init__ (self, id, size): 

        self.identifier = id 
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)
        self.time = 0 
        # Initialiser x comme un vecteur nul
        self.x = np.zeros(size)
    
    def work(self):
        print(f"Task {self.identifier} is processing.")
        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.time = end - start
        print(f"Task {self.identifier} completed in {self.time:.4f} seconds.")

    def to_json(self) -> str:
        task_dict = {
            "id": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "time": self.time,
            "x": self.x.tolist()
        }
        return json.dumps(task_dict)

    @classmethod
    def from_json(cls, text: str) -> "Task":
        task_dict = json.loads(text)
        task = cls(task_dict["id"], task_dict["size"])
        task.a = np.array(task_dict["a"])
        task.b = np.array(task_dict["b"])
        task.time = task_dict["time"]
        task.x = np.array(task_dict["x"])
        return task

    def __eq__(self, other: "Task") -> bool:
        return (self.identifier == other.identifier) and (self.size == other.size) and \
               np.array_equal(self.a, other.a) and np.array_equal(self.b, other.b) and \
               (self.time == other.time) and np.array_equal(self.x, other.x)


