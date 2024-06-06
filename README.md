Opis Projekta
Digitalna Biblioteka je jednostavna aplikacija za upravljanje knjigama. Omogućava korisnicima da dodaju, pretražuju, izmenjuju i brišu knjige, kao i da sačuvaju i učitaju biblioteku iz fajla

Pokretanje Aplikacije
Klonirajte repozitorijum: git clone https://github.com/lipar2/biblioteka.git

Pokretanje apliikacije python src/main.py

Funkcionalnosti  
Dodavanje knjige

Korisnici mogu dodati knjigu unosom naslova, autora, godine izdavanja i žanra. Pretraga knjiga

Korisnici mogu pretraživati knjige po naslovu, autoru, godini izdavanja ili žanru. Izmena informacija o knjizi

Korisnici mogu izmeniti informacije o postojećoj knjizi. Brisanje knjige

Korisnici mogu obrisati knjige iz biblioteke. Rad sa fajlovima

Korisnici mogu sačuvati biblioteku u fajl i učitati biblioteku iz fajla

Struktura
digitalna-biblioteka/ ├── README.md ├── requirements.txt ├── user_stories.md ├── src/ │ ├── book.py │ ├── library.py │ └── main.py └── test/ ├── test_book.py ├── test_library.py └── test_main.py

User Stories
Korisničke priče su navedene u fajlu user_stories.md.

Tehnički Zahtevi
Detaljni tehnički zahtevi su navedeni u fajlu requirements.md.

Testiranje
Aplikacija koristi pristup Test Driven Development-a (TDD). Testovi su locirani u folderu test

Pokretanje testova python -m unittest discover -s test
Autor
Marinko Sukur