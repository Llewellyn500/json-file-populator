import os
import json

# Set the folder path where the PDFs are located
folder_path = 'books/'

# Create an empty list to store the book dictionaries
books = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Get the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Extract the book name from the filename
        book_name = os.path.splitext(filename)[0].replace('_', ' ')
        
        # Create a dictionary for the book
        book = {
            'name': book_name,
            'url': file_path
        }
        
        # Add the book dictionary to the list
        books.append(book)

# Save the list of books to a JSON file
with open('books.json', 'w') as f:
    json.dump(books, f, indent=2)