# Tuples

# 1. Tuple Mastery
# Task 1: Formatting flight itineraries

# (traveler_name, origin, destination)

# declare a tuple with 

# List_of_tuples = ()

# define a function

# ', \n'.join(temp_list) concatenating the string representations of the tuples with a delimiter (using the comma)
# .join is used to concatenate elements of an iterable as its arguement and returns a string where the elements 
# of the iterable are joined together with the string on which it is called.
# An iterable is any iterable object whose elements you want to join together into a string.
flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flight_itinerary_str = ', \n'.join([f"{name} flying from {departure} to {destination}" for name, departure, destination in flight_itinerary])

print(flight_itinerary_str)









# # python tuple() function
# example_tuple = [{"a": "1", "b": "2", "c": "3"}]
# another_tuple = tuple(example_tuple)
# print(another_tuple)






# # using list() to change our tuple
# my_tuple = ("Introduction", "Conclusion")
# temp_list = list(my_tuple)
# temp_list.append("Epilogue")
# my_tuple = tuple(temp_list)
# print(my_tuple)


# # function
# #           parameter
# def greet_user(user):
# #           using the parameter in the function
#     print(f"Hello, {user}")


# 2. Python data Structure Challenges in Real-World Scenarios
# Library System Enhancement




library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# def main():
# while True:

# Step 1. Convert the list of tuples to a set of tuples.
# Using a set automatically remove duplicates since sets won't allow duplicates.

set_of_tuples = set(library)
print(set_of_tuples)

def add_multiple():
# Adding multiple tuples
# update() method allows you to add multiple tuples (as it accepts an itterable).
# get the number of book you want to add to the library
    num_tuple = int(input("Enter the number of books you want to add: "))
# Initialize an empty set to store user input tuples
    tuples_to_add = set()
# Loop to collect tuples from the user
    for i in range(num_tuple):
        book_title = input("Enter a book title: ")
        author = input("Enter the author: ")
        new_tuple = (book_title, author)
        # adding a single tuple (new tuple) to the set tuples_to_add using .add method
        tuples_to_add.add(new_tuple)
# updating the existing library
    for new_tuple in tuples_to_add:
        if new_tuple in set_of_tuples:
            print(f"{new_tuple} is already in the library." )
        
    else:
        set_of_tuples.update(tuples_to_add)
        print(set_of_tuples)

def add_single():
# add a book and author via user input
    book_title = input("Enter a book title: ")
    author = input("Enter the author: ")
    new_tuple = (book_title, author)
# Checking to see if book already entered in library
    if new_tuple in set_of_tuples:
        print("Book already in library.")
    else:
# add new book to library
        set_of_tuples.add(new_tuple)
        print("book added.")

print("Updated library:", set_of_tuples)

# View library
def view_library():
    print(set_of_tuples)


# Driver Code
def main():
   while True:
    response = input("""
                     Type '1' to add a single book.
                     Type '2' to add multiple books.
                     Type '3' to view library.
                     Type 'quit' to quit.
""")
    if response == "1":
        add_single()

    elif response == ("2"):
        add_multiple()

    elif response == ("3"):
        view_library()
    
    else:
        response == 'quit'
        break
        
main()


# Mastering Tuple Packing and Unpacking in Python
# Customer order processing



orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Unpacking a list of tuples involves iterating over each tuple in the list and
# unpacking each tuple into individual variables.

for tuple_item in orders:
    customer, item, quantity = tuple_item
    print("Customer: ", customer)
    print("Item: ", item)
    print("Quantity: ", quantity)
