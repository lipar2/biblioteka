import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Book

class Test_Book(unittest.TestCase):
    def test_dodavanje_naslova(self):
        b = Book("Na Drini cuprija", " ", 1954, " ")
        self.assertEqual(b.naziv, "Na Drini cuprija")

    def test_dodavanje_autora(self):
        b = Book("Na Drini cuprija", "Ivo Andric", 1954, " ")
        self.assertEqual(b.autor, "Ivo Andric")
    
    def test_dodavanje_godine_izdanja(self):
        b = Book("Na Drini cuprija", "Ivo Andric", 1954, " ")
        self.assertEqual(b.god_izdanja, 1954)

    def test_dodavanje_zanra(self):
        b = Book("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(b.zanr, "Roman")