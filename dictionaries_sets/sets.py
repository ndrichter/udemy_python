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

# all items present in both sets
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
