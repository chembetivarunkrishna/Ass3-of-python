# SET OPERATIONS
# Create a set from a list (removes duplicates automatically)
numbers = [1, 2, 3, 4, 5, 2, 3, 6]
set1 = set(numbers)

print("Original Set:", set1)

# Add new elements
set1.add(7)
set1.add(8)
print("After Adding Elements:", set1)

# Remove elements
set1.remove(3)      # removes 3
print("After Removing Element:", set1)

# Another set for operations
set2 = {4, 5, 6, 7, 9}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))
# LIBRARY MANAGEMENT USING DICTIONARY

library = {}

# Function to add a book
def add_book(title, author, year, genre):
    library[title] = {
        "Author": author,
        "Publication Year": year,
        "Genre": genre
    }
    print(f"'{title}' added successfully.")

# Function to display all books
def display_books():
    if not library:
        print("Library is empty.")
    else:
        for title, details in library.items():
            print("\nTitle:", title)
            for key, value in details.items():
                print(f"{key}: {value}")

# Function to search a book
def search_book(title):
    if title in library:
        print("\nBook Found:")
        print(library[title])
    else:
        print("Book not found.")

# Function to remove a book
def remove_book(title):
    if title in library:
        del library[title]
        print(f"'{title}' removed successfully.")
    else:
        print("Book not found.")

# Adding books
add_book("Python Basics", "John Smith", 2022, "Programming")
add_book("Data Science", "Alice Brown", 2021, "Education")

# Display books
display_books()

# Search for a book
search_book("Python Basics")

# Remove a book
remove_book("Data Science")

# Display updated library
display_books()