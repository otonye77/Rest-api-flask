# name = "Bob"
# greetings = f"Hello, {name}"
# print(greetings)

# name = "Bob"
# greetings = "Hello, {}"
# print(greetings.format(name))

# long_string = "Hello, {}. My name is {}"
# print(long_string.format("Guys", "Peter"))

# name = input("What is your name: ")
# print(name)

# num1 = input("Your first digit: ")
# num2 = input("Your second digit: ")
# answer = float(num1) * float(num2)
# print(answer)

# l = ["Otonye", "Blossom"]
# t = ("Otonye", "Blossom")
# s = {"Otonye", "Blossom"} 

# friends = {"Peter", "John", "James"}
# abroad = {"James", "John"}

# set1 = {14, 5, 9, 31, 12, 77, 67, 8}
# set2 = {5, 77, 9, 12}
# print(set1.intersection(set2))

# total_friends = friends.union(abroad)
# print(total_friends)

# local_friends = friends.difference(abroad) 
# print(local_friends)

# day_of_week = input("What day of the week is it today? ")
# if day_of_week == "Monday":
#     print("Then we will learn Mathematics")
# elif day_of_week =="Wednesday":
#     print("Holiday Time")
# else:
#     print("Stand Up")

# l = ["Paul", "Ralph", "John"]
# print("Paul" in l)


# movies_watched = {"The Matrix", "Friends", "Ant-Man"}
# movie = input("Tell me a movies you have watched before? ")
# if(f"{movie}" in movies_watched):
#     print(f"You have seen {movie} Before Boy")
# else:
#     print(f"You can watch {movie} boy")

# magic_number = 7
# consent = input("Do you wish to play our game? Enter Y if Yes or N if No ")
# if(f"{consent}" == "Y"):
#     guess = input("What is the magic number? ")
#     user_input = int(guess)
#     if(user_input == magic_number):
#         print("Congratulation you have won the game")
#     else:
#         print("Please try again tomorrow")
# elif(f"{consent}" == "N"):
#     print("Okay then you can control c now")

# friends = ["Joey", "Chandlier", "Monica", "Rachael"]
# for friend in friends:
#     print(friend)

# numbers = [10, 8, 7, 12]
# total = 0
# for number in numbers:
#     total = total + number
# print(total)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# evens = []
# for number in numbers:
#     if number % 2 == 0:
#         evens.append(number)
# print(evens)

# array = [1, 2, 3]
# emp = []
# for num in array:
#     emp.append(num * 2)
# print(emp)

# friends =[
#     {"Name": "James", "Age": 27, "Hobby": "Smoking"},
#     {"Name": "Peace", "Age": 24, "Hobby": "Drinking"},
#     {"Name": "Pape", "Age": 28, "Hobby": "Gambling"}
#     ]
# for friend in friends:
#     if friend["Name"] == "Peace":
#         print("I am peace")

# def Hello():
#     print("Print Hello")

# Hello()

# friends = []
# def add_friend(person):
#     if person not in friends:
#         friends.append(person)
# add_friend("Moses")
# add_friend("Paul")
# add_friend("Moses")
# print(friends)

# def divisor(dividend, divisor):
#     if isinstance(divisor, (int, float)) and divisor != 0:
#         answer = dividend / divisor
#         return answer
#     else:
#         return "You Fool. Stop that."

# print(divisor(15, "5"))

# l = [9, 0, 2]
# def multiply_two(x):
#     return x * 2
# doubled = list(map(multiply_two, l))
# print(doubled)

# def multiply(*args):
#     print(args)
# multiply(1,2,3)

# def named(**kwargs):
#     print(kwargs)

# Object Oriented Programming

# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (65, 80, 93.9, 92.7, 73.9)

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student = Student()
# print(student.name)
# print(student.average())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#        return f"{self.name} is {self.age}"
# bob = Person("Bob", 37)
# print(bob)

# class Book:
#     TYPES = ("hardcover", "paperback")
#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight
    
#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type}, {self.weight} g>"
    
#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return Book(name, Book.TYPES[0], page_weight + 100)
    
#     @classmethod
#     def paperback(cls, name, page_weight):
#         return Book(name, Book.TYPES[1], page_weight)

# book = Book.hardcover("Harry Potter", 1700)

# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True
#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"
#     def disconnect(self):
#         self.connected = False
#         print("Disconnected")

# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_page = capacity
    
class BookShelf:
    def __init__(self, *book):
        self.book = book

    def __str__(self):
        return f"Bookshelf with {len(self.book)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)