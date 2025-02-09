import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        self.assertNotEqual(englishToFrench("Hello"), "Bonjourno")


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Hallo") 

unittest.main()