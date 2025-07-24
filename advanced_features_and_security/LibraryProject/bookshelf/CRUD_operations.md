# Import the Book model
from bookshelf.models import Book

# ----------------------------------------
# ✅ 1. Creating a Book instance
# ----------------------------------------

# Create and save a new Book instance in the database
book = Book.objects.create(
    title='1984',
    author='George Orwell',
    publication_year=1949
)
print("Created book:", book)

# ----------------------------------------
# ✅ 2. Retrieving and displaying all books
# ----------------------------------------

# Retrieve all books in the database
books = Book.objects.all()
print("All books:", books)

# Retrieve the book we just created using a specific field
book = Book.objects.get(title='1984')
print("Retrieved book:", book)

# ----------------------------------------
# ✅ 3. Updating the book title
# ----------------------------------------

# Update the title of the retrieved book instance
book.title = 'Nineteen-Eighty-Four'
book.save()  # Always call save() to apply changes to the database
print("Updated book title:", book.title)

# ----------------------------------------
# ✅ 4. Deleting the book
# ----------------------------------------

# Delete the book from the database
deleted_count, deleted_objects = book.delete()
print(f"Deleted {deleted_count} object(s):", deleted_objects)

# Confirm deletion
books = Book.objects.all()
print("All books after deletion:", books)
