# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name)
#         print(self.age)
# # creating object


# user1 = User("John Doe", 30)
# print(user1.name)
# print(user1.age)

# user1.display()


class Employee:
    name = "John Doe"
    age = 30

    def display(self):
        print(self.name)
        print(self.age)


# creating object
emp1 = Employee()
print(emp1.name)
print(emp1.age)

emp1.display()


class User:
    species = "Human"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute


user1 = User("Alice")
user2 = User("Bob")

print(user1.species)  # Human
print(user2.species)  # Human

user1.species = "Alien"
print(user1.species)  # Alien
print(user2.species)  # Human

print(user1.species)  # Alien
print(user2.species)  # Human

user2.species = "Alien"
print(user1.species)  # Alien
print(user2.species)  # Alien
