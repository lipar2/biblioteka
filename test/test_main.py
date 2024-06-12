import unittest
import os

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.file_path = "test_file.txt"
        with open(self.file_path, "w") as file:
            file.write("initial content\n")

    def tearDown(self):
        os.remove(self.file_path)

    def test_citanja_i_pisanja(self):
        # Dodajemo "volkswagen" na kraj fajla
        with open(self.file_path, "a") as file:
            file.write("volkswagen\n")
        
        # Provera da li je "volkswagen" dodat u fajl
        with open(self.file_path, "r") as file:
            provera = False
            lines = file.readlines()
            for line in lines:
                if line.strip() == "volkswagen":
                    provera = True
            self.assertTrue(provera)
        
        # Brišemo "volkswagen" iz fajla
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                if line.strip() != "volkswagen":
                    file.write(line)
        
        # Provera da li je "volkswagen" uspešno obrisan iz fajla
        with open(self.file_path, "r") as file:
            provera = False
            lines = file.readlines()
            for line in lines:
                if line.strip() == "volkswagen":
                    provera = True
            self.assertFalse(provera)

if __name__ == '__main__':
    unittest.main()
