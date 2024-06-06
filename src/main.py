from library import Library
from book import Book
library = Library()

unos = input("Sta zelite da radite? (1-Za dodavanje knjige, 2-Za pretrazivanje knjige, 3-Za menjanje informacija o knjigama, 4-Za prikaz svih knjiga): ")
if unos =="1":
    while True:
        print("Napisi informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        knjiga = Book(naziv, autor, god_izdanja, zanr)
        library.dodaj_knjigu(knjiga)
        prekid = input("za prekid stisni start")
        if prekid == "start":
            break
    
    with open("fajl.txt", "a") as file:
        for object in library.lista_objekata:
            file.write(object.display_info() + "\n")

elif unos == "2":
    kriterijum = input("Po cemu zelite da pretrazujete: ")
    key_word = input("Kljucna rec za pretragu: ")
    results = library.search_books(kriterijum, key_word)
    print("Rezultati pretrage: ")
    for result in results:
        print(result)

elif unos == "3":
    print("Napisi informacije o knjizi koju zelite da izmenite.")
    naziv = input("Naziv: ")
    autor = input("Autor: ")
    god_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    knjiga = Book(naziv, autor, god_izdanja, zanr)

    print("Napisi informacije o izmenjenoj knjizi.")
    naziv1 = input("Naziv: ")
    autor1 = input("Autor: ")
    god_izdanja1 = input("Godina izdanja: ")
    zanr1 = input("Zanr: ")
    knjiga1 = Book(naziv1, autor1, god_izdanja1, zanr1)

    with open("fajl.txt", "r") as file:
        lines = file.readlines()
    
    lines = [knjiga1.display_info() + '\n' if knjiga.display_info() in line else line for line in lines]
    with open("fajl.txt", "w") as file:
        file.writelines(lines)

elif unos == "4":
    print("Napisi informacije o knjizi koju zelite da izbrisete.")
    naziv = input("Naziv: ")
    autor = input("Autor: ")
    god_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    knjiga = Book(naziv, autor, god_izdanja, zanr)
    with open("fajl.txt", "r") as file:
        lines = file.readlines()
    with open("fajl.txt", "w") as file:
        for line in lines:
            if line.strip() != knjiga.display_info().strip():
                file.write(line)