import random
from collections import Counter

def generate_random_list(size, min_value, max_value):
  
    random_list = [random.randint(min_value, max_value) for _ in range(size)]
    return random_list

def most_frequent(lst):
    lst.sort() 
    max_count = 0
    most_common = None
    current_count = 0
    current_element = None

    for element in lst:
        if element == current_element:
            current_count += 1
        else:
            current_element = element
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            most_common = current_element

    return most_common
random_list = generate_random_list(20, 1, 10)
print("Random List:", random_list)

most_common_element = most_frequent(random_list)
print("The most frequently occurring element is:", most_common_element)

