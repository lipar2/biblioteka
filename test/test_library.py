from io import StringIO
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library
from book import Book

class Test_Libary(unittest.TestCase):
    def test_cuvanje_knjige(self):
        b = Book("dd", "dd", 167, "dd")
        b2 = Book("dd", "dd", 167, "dd")
        l = Library()
        l.dodaj_knjigu(b)
        l.dodaj_knjigu(b2)
        self.assertEqual(len(l.lista_objekata), 2)