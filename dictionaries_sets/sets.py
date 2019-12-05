farm_animals = {"sheep", "cow", "hen"}

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant"])

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

empty_set = set()
empty_dict = {}

# order not guaranteed
even = set(range(0, 40, 2))
print(even)

print(len(even))

squares_tuple = (4, 6,  9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# all items in each set
print(even.union(squares))
print(len(even.union(squares)))

print("=" * 40)

# numbers that are present in both sets
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("=" * 40)

# removing from sets
print(sorted(even))
print(sorted(squares))
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

# update existing set
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# items in either set but not in both
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

# remove specific items in set
print("=" * 40)
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# squares.remove(8) will raise an error, item needs to be in set

even = set(range(0, 40, 2))
print(even)

squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

# frozen sets,  immutable
even = frozenset(range(0, 100, 2))
# even.add(3) will error
