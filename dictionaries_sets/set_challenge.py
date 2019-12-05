# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.


user_input = set(input("Please enter a phrase  ").lower().replace(" ", ""))
# vowels = {"a", "e", "i", "o", "u"}
vowels = frozenset("aeiou")

print(user_input)

user_input.difference_update(vowels)

print(sorted(user_input))
