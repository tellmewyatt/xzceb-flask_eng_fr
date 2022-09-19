import unittest
import translator
class testEnglishToFrench(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")
    def test_my_friends(self):
        self.assertEqual(translator.englishToFrench("My friends"), "Mes amis")
    def test_everybody_in_the_club(self):
        self.assertEqual(translator.englishToFrench("Everybody in the club"), "Tout le monde dans le club")
    def test_null(self):
        self.assertEqual(translator.englishToFrench(None), "") # Null Case
class testFrenchToEnglish(unittest.TestCase):
    def test_bonjour(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")
    def test_mes_amis(self):
        self.assertEqual(translator.frenchToEnglish("Mes amis"), "My Friends")
    def test_tout_le_monde_dans_le_club(self):
        self.assertEqual(translator.frenchToEnglish("Tout le monde dans le club"), "Everyone in the club")
    def test_null(self):
        self.assertEqual(translator.frenchToEnglish(None), "") # Null Case
unittest.main()