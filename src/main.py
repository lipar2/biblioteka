from library import Library
from book import Book

def dodaj_knjigu(library):
    while True:
        print("Unesite informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        knjiga = Book(naziv, autor, god_izdanja, zanr)
        library.dodaj_knjigu(knjiga)
        prekid = input("Za prekid unesite 'start': ")
        if prekid == "start":
            break

    with open("fajl.txt", "a") as file:
        for book in library.lista_objekata:
            file.write(book.display_info() + "\n")

def pretrazi_knjige(library):
    kriterijum = input("Po čemu želite da pretražujete: ")
    key_word = input("Ključna reč za pretragu: ")
    results = library.search_books(kriterijum, key_word)
    print("Rezultati pretrage: ")
    for result in results:
        print(result)

def izmeni_knjigu(library):
    print("Unesite informacije o knjizi koju želite da izmenite.")
    stari_naziv = input("Stari naziv: ")

    print("Unesite nove informacije o knjizi.")
    novi_naziv = input("Novi naziv: ")
    novi_autor = input("Novi autor: ")
    nova_god_izdanja = input("Nova godina izdanja: ")
    novi_zanr = input("Novi zanr: ")

    library.izmeni_knjigu(stari_naziv, novi_naziv, novi_autor, nova_god_izdanja, novi_zanr)

def prikazi_knjige(library):
    print("Sve knjige u biblioteci:")
    library.ispis_knjiga()

def obrisi_knjigu(library):
    print("Unesite informacije o knjizi koju želite da izbrišete.")
    naziv = input("Naziv: ")
    library.obrisi_knjigu(naziv)

def izlaz(library):
    print("Izlaz iz programa.")
    exit()

def main():
    library = Library()

    opcije = {
        "1": dodaj_knjigu,
        "2": pretrazi_knjige,
        "3": izmeni_knjigu,
        "4": prikazi_knjige,
        "5": obrisi_knjigu,
        "0": izlaz
    }

    while True:
        unos = input("Šta želite da radite? (1-Dodaj knjigu, 2-Pretraži knjige, 3-Izmeni knjigu, 4-Prikaži sve knjige, 5-Izbriši knjigu, 0-Izlaz): ")
        opcija = opcije.get(unos)
        if opcija:
            opcija(library)
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()
