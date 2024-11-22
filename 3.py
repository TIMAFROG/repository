class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def raed_chapter(self, chapter_number):
        print(f'Глава {chapter_number} прочитана')


b = Book('Book', 'Author', 999)
b.raed_chapter(4)
