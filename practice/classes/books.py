class Books():
    def __init__(self, author,  book_title, year_publication='2000'):
            self.set_author(author)
            self.set_title(book_title)
            self._set_year(year_publication)

    def show_book(self):
        print(self._book_title+', "'+self._author+'", '+self._year)

    def set_title(self, title):
        self._book_title = title

    def set_author(self, author):
        self._author = author

    def _set_year(self, year):
        self._year = year


title = input('book title')
author = input('book author')
year =  input('year of publish')
b1 = Books(author, title, year)
b1.show_book()
b1._set_year('2015')
b1.show_book()