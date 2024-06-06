import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class Test_Main(unittest.TestCase):
   def test_citanja(self):
      with open("fajl.txt", "a") as file:
         file.write("\nvolkswagen")

      with open("fajl.txt", "r") as file:
         provera = False
         lines = file.readlines()
         for line in lines:
            if line == "volkswagen":
               provera = True
        
         self.assertTrue(provera)
    
      with open("fajl.txt", "w") as file:
         for line in lines:
            if line != "volkswagen":
               file.write(line)

         
            

if __name__ == '__main__':
   unittest.main()   