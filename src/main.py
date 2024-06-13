from library import Library
from book import Book

class MenadzerBiblioteka:
    def __init__(self):
        self.biblioteke = []

    def dodaj_biblioteku(self, naziv):
        nova_biblioteka = Library(naziv)
        self.biblioteke.append(nova_biblioteka)

    def obrisi_biblioteku(self, naziv):
        self.biblioteke = [biblioteka for biblioteka in self.biblioteke if biblioteka.naziv != naziv]

    def broj_biblioteka(self):
        return len(self.biblioteke)

    def dodaj_knjigu(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                while True:
                    print("Unesite informacije o knjizi.")
                    naziv = input("Naziv: ")
                    autor = input("Autor: ")
                    god_izdanja = input("Godina izdanja: ")
                    zanr = input("Zanr: ")
                    knjiga = Book(naziv, autor, god_izdanja, zanr)
                    biblioteka.dodaj_knjigu(knjiga)
                    prekid = input("Za prekid unesite 'start': ")
                    if prekid == "start":
                        break
                break

    def pretrazi_knjige(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                kriterijum = input("Po čemu želite da pretražujete: ")
                key_word = input("Ključna reč za pretragu: ")
                results = biblioteka.search_books(kriterijum, key_word)
                print("Rezultati pretrage: ")
                for result in results:
                    print(result)
                break

    def izmeni_knjigu(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                print("Unesite informacije o knjizi koju želite da izmenite.")
                stari_naziv = input("Stari naziv: ")

                print("Unesite nove informacije o knjizi.")
                novi_naziv = input("Novi naziv: ")
                novi_autor = input("Novi autor: ")
                nova_god_izdanja = input("Nova godina izdanja: ")
                novi_zanr = input("Novi zanr: ")

                biblioteka.izmeni_knjigu(stari_naziv, novi_naziv, novi_autor, nova_god_izdanja, novi_zanr)
                break

    def prikazi_knjige(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                print("Sve knjige u biblioteci:")
                biblioteka.ispis_knjiga()
                break

    def obrisi_knjigu(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                print("Unesite informacije o knjizi koju želite da izbrišete.")
                naziv = input("Naziv: ")
                biblioteka.obrisi_knjigu(naziv)
                break

    def broj_knjiga_u_biblioteci(self, naziv_biblioteke):
        for biblioteka in self.biblioteke:
            if biblioteka.naziv == naziv_biblioteke:
                return biblioteka.broj_knjiga()

def izlaz():
    print("Izlaz iz programa.")
    exit()

def main():
    library_manager = MenadzerBiblioteka()

    opcije = {
        "1": library_manager.dodaj_biblioteku,
        "2": library_manager.obrisi_biblioteku,
        "3": lambda: print(f"Broj biblioteka: {library_manager.broj_biblioteka()}"),
        "4": library_manager.dodaj_knjigu,
        "5": library_manager.pretrazi_knjige,
        "6": library_manager.izmeni_knjigu,
        "7": library_manager.prikazi_knjige,
        "8": library_manager.obrisi_knjigu,
        "9": lambda: print(f"Broj knjiga u biblioteci: {library_manager.broj_knjiga_u_biblioteci(input('Naziv biblioteke: '))}"),
        "0": izlaz
    }

    while True:
        print("Opcije: \n1-Dodaj biblioteku \n2-Obriši biblioteku \n3-Broj biblioteka \n4-Dodaj knjigu \n5-Pretraži knjige \n6-Izmeni knjigu \n7-Prikaži sve knjige \n8-Izbriši knjigu \n9-Broj knjiga u biblioteci \n0-Izlaz")
        unos = input("Šta želite da radite? ")
        opcija = opcije.get(unos)
        if opcija:
            if unos in ["1", "2", "4", "5", "6", "7", "8"]:
                naziv = input("Naziv biblioteke: ")
                opcija(naziv)
            else:
                opcija()
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()
