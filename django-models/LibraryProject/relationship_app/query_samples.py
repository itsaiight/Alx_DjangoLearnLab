from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name = author_name)
    books = Book.objects.filter(author = author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library.name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"The librarian for {library.name} is {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or Librarian not found.")
