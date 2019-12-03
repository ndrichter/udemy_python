# dict: unordered and no duplicates


fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])

# add entry
fruit["pear"] = "an odd shaped apple"
print(fruit)

# update/overwrite value
fruit["lime"] = "great with tequila"
print(fruit)

# delete key / value
del fruit["lemon"]
print(fruit)

# remove all keys from dict
# fruit.clear()
# print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have {}".format(dict_key))
    print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have {}".format(dict_key))

# no guarantee same order provided from dict by default
for snack in fruit:
    print(fruit[snack])

# sorted keys
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# returns list like objects
print(fruit.keys())
print(fruit.values())
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)