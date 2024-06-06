import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Book

class Test_Book(unittest.TestCase):
    def test_dodavanje_naslova(self):
        sarmin = Book("Drugi svetski rat", " ", 1939, " ")
        self.assertEqual(sarmin.naziv, "Drugi svetski rat")

    def test_dodavanje_autora(self):
        knj = Book("Mali Princ", "Ivo Andric", 1233, " ")
        self.assertEqual(knj.autor, "Ivo Andric")
    
    def test_dodavanje_godine_izdanja(self):
        knji = Book("Istorija Srba", "Ivo Andric", 1759, " ")
        self.assertEqual(knji.god_izdanja, 1759)

    def test_dodavanje_zanra(self):
        knjig = Book("Jedna zelja jedna Nada", "Dusan Dzakic", 1152, "Roman")
        self.assertEqual(knjig.zanr, "Roman")

    def test_displayinfo(self):
        knjiga = Book("d", "d", 1954, "d")
        self.assertEqual(knjiga.display_info(), "d, d, 1954, d")

if __name__ == '__main__':
   unittest.main()