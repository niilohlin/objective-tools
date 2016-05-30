import unittest
from stats import *
from files import *

class Tests(unittest.TestCase):

    @staticmethod
    def listOfOCClasses():
        return [
                ObjectiveCClass(publicMethods=4, className="TestClass4"),
                ObjectiveCClass(publicMethods=5, className="TestClass5"),
                ObjectiveCClass(publicMethods=2, className="TestClass2"),
                ObjectiveCClass(publicMethods=1, className="TestClass1"),
                ObjectiveCClass(publicMethods=4, className="TestClass3")]

    def test_headersIsClass(self):
        self.assertEqual(headers()[0], "class.h")

    def test_propertiesIs4(self):
        self.assertEqual(parseFile("class.h"), ObjectiveCClass(publicMethods=4, className="TestClass"))


    def test_average(self):
        self.assertEqual(calculateAveragePublic([ObjectiveCClass(publicMethods=5, className="")]), 5)

    def test_findWorst(self):
        classes = Tests.listOfOCClasses()
        self.assertEqual(findMostPublic(classes, 1), [ObjectiveCClass(publicMethods=5, className="TestClass5")])

    def test_subString(self):
        self.assertEqual(subStringOfMatching('{', '}', "kala{sKu{}ng}en"), "sKu{}ng")



if __name__ == "__main__":
    unittest.main()

