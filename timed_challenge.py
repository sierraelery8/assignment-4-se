# Pick one question from timed_challenge.txt
# 3. Remove Duplicates (Keep Order)

# Paste the question as a comment below

# Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]


# Solution

def remove_duplicates(values):
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


# Test cases

print(remove_duplicates(["apple", "banana", "apple", "kiwi", "banana"]))
print(remove_duplicates([1, 2, 3, 2, 1]))
print(remove_duplicates([]))
print(remove_duplicates(["a", "a", "a"]))


"""
Reflection:

I chose a combination of a set and a list for this challenge because the problem
required removing duplicates while also keeping the original order of the values.
A set allowed me to quickly check whether a value had already been seen, while
the list stored the values in the order they appeared. This structure choice
allowed me to solve the problem efficiently while meeting the requirements.

The 30-minute time limit influenced my decision because I focused on selecting
a simple and reliable solution instead of trying to create something overly
complex. During a technical interview, choosing the correct data structure and
explaining the reasoning behind the choice is important.

One trade-off I made was using extra memory because I needed both a set and a
list. While this uses more space, it improves efficiency by avoiding repeatedly
searching through the list for duplicate values. Under time pressure, I
prioritized creating code that was readable, correct, and easy to explain.
"""