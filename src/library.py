from book import Book

class Library:
    def __init__(self):
        self.lista_objekata = []

    def dodaj_knjigu(self, book):
        self.lista_objekata.append(book)

    def ispis_knjiga(self):
        for book in self.lista_objekata:
            print(book)

    def search_books(self, search_criteria, keyword):
        results = []
        with open("fajl.txt", "r") as file:
            for line in file:
                book_data = line.strip().split(", ")
                book = Book(*book_data)
                if search_criteria.lower() == "naslov" and keyword.lower() in book.naziv.lower():
                    results.append(book)
                elif search_criteria.lower() == "autor" and keyword.lower() in book.autor.lower():
                    results.append(book)
                elif search_criteria.lower() == "godina" and keyword == book.god_izdanja:
                    results.append(book)
                elif search_criteria.lower() == "zanr" and keyword.lower() in book.zanr.lower():
                    results.append(book)
        return results

    def izmeni_knjigu(self, stari_naziv, novi_naziv, novi_autor, nova_god_izdanja, novi_zanr):
        with open("fajl.txt", "r") as file:
            lines = file.readlines()

        with open("fajl.txt", "w") as file:
            for line in lines:
                book_data = line.strip().split(", ")
                if book_data[0] == stari_naziv:
                    file.write(f"{novi_naziv}, {novi_autor}, {nova_god_izdanja}, {novi_zanr}\n")
                else:
                    file.write(line)

    def obrisi_knjigu(self, naziv):
        with open("fajl.txt", "r") as file:
            lines = file.readlines()

        with open("fajl.txt", "w") as file:
            for line in lines:
                if not line.startswith(naziv):
                    file.write(line)
