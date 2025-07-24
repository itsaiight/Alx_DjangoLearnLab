# Updating the title of Book

book.title = "Nineteen Eighty-Four"
book.save()  # Always call save() to apply changes to the database
print("Updated book title:", book.title)


Alternatively 

# This method does not require save()
book = Book.objects.update(title = "Nineteen Eighty-Four")
