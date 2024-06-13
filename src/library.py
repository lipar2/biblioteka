from book import Book

class Library:
    def __init__(self, naziv):
        self.naziv = naziv
        self.lista_objekata = []

    def dodaj_knjigu(self, book):
        self.lista_objekata.append(book)

    def ispis_knjiga(self):
        for book in self.lista_objekata:
            print(book.display_info())

    def search_books(self, search_criteria, keyword):
        results = []
        for book in self.lista_objekata:
            if search_criteria.lower() == "naslov" and keyword.lower() in book.naziv.lower():
                results.append(book.display_info())
            elif search_criteria.lower() == "autor" and keyword.lower() in book.autor.lower():
                results.append(book.display_info())
            elif search_criteria.lower() == "godina" and keyword == book.god_izdanja:
                results.append(book.display_info())
            elif search_criteria.lower() == "zanr" and keyword.lower() in book.zanr.lower():
                results.append(book.display_info())
        return results

    def izmeni_knjigu(self, stari_naziv, novi_naziv, novi_autor, nova_god_izdanja, novi_zanr):
        for book in self.lista_objekata:
            if book.naziv == stari_naziv:
                book.naziv = novi_naziv
                book.autor = novi_autor
                book.god_izdanja = nova_god_izdanja
                book.zanr = novi_zanr
                break

    def obrisi_knjigu(self, naziv):
        self.lista_objekata = [book for book in self.lista_objekata if book.naziv != naziv]

    def broj_knjiga(self):
        return len(self.lista_objekata)
