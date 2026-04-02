
import unittest
import person





class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = person.Person("Имя", 10)

    def testPrint(self):
        self.assertEqual(self.person.printName(),"Имя: Имя")
        self.assertEqual(self.person.printAge(), "Возвраст: 10")

if __name__ == '__main__':
    unittest.main()

