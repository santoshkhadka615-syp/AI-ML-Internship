"""
Week 1 - Beginner Python Exercises
Covers: lists, dicts, loops, functions, file I/O
"""

# 1. Sum of a list
def sum_list(numbers):
    return sum(numbers)


# 2. Find the maximum number in a list
def find_max(numbers):
    return max(numbers)


# 3. Reverse a string
def reverse_string(text):
    return text[::-1]


# 4. Check if a string is a palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


# 5. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)


# 6. Factorial of a number (using loop)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 7. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 8. Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


# 9. Remove duplicates from a list
def remove_duplicates(items):
    return list(set(items))


# 10. Count occurrences of each word in a sentence (using dict)
def word_count(sentence):
    words = sentence.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


# 11. Merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# 12. Find common elements between two lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# 13. Sort a list of dictionaries by a key
def sort_by_key(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])


# 14. Flatten a nested list
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# 15. Simple class using OOP basics
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name}: avg = {self.average():.2f}"


# 16. Write a list of numbers to a file
def write_numbers_to_file(numbers, filename="numbers.txt"):
    with open(filename, "w") as f:
        for num in numbers:
            f.write(f"{num}\n")


# 17. Read numbers from a file and return their sum
def read_and_sum_file(filename="numbers.txt"):
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    return sum(numbers)


# 18. Count total lines and words in a text file
def file_stats(filename="numbers.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    return total_lines, total_words


