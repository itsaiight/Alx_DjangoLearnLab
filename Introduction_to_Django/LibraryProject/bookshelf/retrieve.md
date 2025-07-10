Retrieving and displaying all attributes of the book the was created

# Retrieve all books
books = Book.objects.all()
print("All books:", books)

# Retrieve the book we just created using a specific field
book = Book.objects.get(title='1984')
print("Retrieved book:", book)