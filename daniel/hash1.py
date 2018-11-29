#!/usr/bin/python3

#   name1="Shubham"
#   name2="Shubham!"
#   hash1=hash(name1)
#   hash2=hash(name2)
#
#   print("Hash 1: %s" % hash1)
#   print("Hash 2: %s" % hash2)


class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        return hash((self.age, self.name))

student = Student(23, 'Shubham')
print("The hash is: %d" % hash(student))
