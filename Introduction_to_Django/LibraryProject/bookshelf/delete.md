Deleting the book

# Delete the book from the database
deleted_count, deleted_objects = book.delete()
print(f"Deleted {deleted_count} object(s):", deleted_objects)

# Confirm deletion
books = Book.objects.all()
print("All books after deletion:", books)