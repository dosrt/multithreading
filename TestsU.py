import unittest
import Task 

class TestTaskEquality(unittest.TestCase):

    def test_equality_after_serialization(self):
        # Instanciation de la première Task
        a = Task(1, 3)
        a.work()

        # Sérialisation et désérialisation pour obtenir la seconde Task
        txt = a.to_json()
        b = Task.from_json(txt)

        # Vérification de l'égalité
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
