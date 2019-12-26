from player import Player

nate = Player("Nate")

print(nate.name)
print(nate.lives)
nate.lives -= 1
print(nate)

nate.lives -= 1
print(nate)

nate.lives -= 1
print(nate)

nate.lives = 9
print(nate)

nate.level = 2
print(nate)

nate.level += 5
print(nate)

nate.level -= 3
print(nate)

nate.score = 500
print(nate)
