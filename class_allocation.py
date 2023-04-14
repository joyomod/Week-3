# You are tasked with calculating the minimum classes we need to have, so we know how many people to employ.
# Write a function which when given a number of students, calculates and prints out a string for your proposed
# number of classes, and a dictionary showing the allocation.

# Key Constraints:
# ●	The maximum size of a class is 30
# ●	There needs to be a minimum of 2 classes
# ●	The distribution of each class should be as even as possible.
# ●	We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
import math


def minimum_number_of_classes(num_of_students):
    max_class_size = 30
    num_classes = (num_of_students / max_class_size)
    size_per_class = (num_of_students / num_classes)
    bigger_classes = num_of_students % size_per_class

    # storing class allocation
    allocation = {}

    # students allocation per size
    for i in range(math.ceil(num_classes)):
        if i < bigger_classes:
            allocation[f"Class {i+1}"] = math.ceil(size_per_class)
        else:
            allocation[f"Class {i+1}"] = math.ceil(size_per_class) - 1

    print(f"Number of classes are: {math.ceil(num_classes)}")
    print(f'They are shared like so: {allocation}')


minimum_number_of_classes(100)
