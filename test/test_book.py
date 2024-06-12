import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Drugi svetski rat", "Culibrk Dragan", 1939, "tragedija")
        self.book2 = Book("Mali Princ", "Ivo Andric", 1233, "komedija")
        self.book3 = Book("Istorija Srba", "Antoan de Sent Egziper", 1759, "horor")
        self.book4 = Book("Jedna želja jedna nada", "Dušan Džakić", 1152, "Roman")
        self.book5 = Book("d", "d", 1954, "d")

    def test_dodavanje_naslova(self):
        self.assertEqual(self.book1.naziv, "Drugi svetski rat")

    def test_dodavanje_autora(self):
        self.assertEqual(self.book2.autor, "Ivo Andric")

    def test_dodavanje_godine_izdanja(self):
        self.assertEqual(self.book3.god_izdanja, 1759)

    def test_dodavanje_zanra(self):
        self.assertEqual(self.book4.zanr, "Roman")

    def test_display_info(self):
        self.assertEqual(self.book5.display_info(), "d, d, 1954, d")

if __name__ == '__main__':
    unittest.main()
