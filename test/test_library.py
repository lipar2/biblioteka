from io import StringIO
import unittest
from unittest.mock import patch
import sys
import os

# Dodavanje putanje src foldera kako bi se mogli importovati moduli
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Prva knjiga", "Autor 1", 2000, "Žanr 1")
        self.book2 = Book("Druga knjiga", "Autor 2", 2010, "Žanr 2")

    def tearDown(self):
        # Resetovanje stdout na sys.stdout nakon svakog testa
        sys.stdout = sys.__stdout__

    def test_dodavanje_knjige(self):
        self.library.dodaj_knjigu(self.book1)
        self.library.dodaj_knjigu(self.book2)
        self.assertEqual(len(self.library.lista_objekata), 2)

    def test_ispis_knjiga(self):
        self.library.dodaj_knjigu(self.book1)
        self.library.dodaj_knjigu(self.book2)
        
        capture_output = StringIO()
        sys.stdout = capture_output
        
        self.library.ispis_knjiga()
        
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue().strip(), "Prva knjiga, Autor 1, 2000, Žanr 1\nDruga knjiga, Autor 2, 2010, Žanr 2")

if __name__ == '__main__':
    unittest.main()
