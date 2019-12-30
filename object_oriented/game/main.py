from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

nate = Player("Nate")

ugly_troll = Troll("Pug")
print("Ugly Troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

ugly_troll.take_damage(2)

nasty_vampire = Vampire("Nosferatu")
print(nasty_vampire)

# while nasty_vampire._alive:
#     nasty_vampire.take_damage(2)
#     print(nasty_vampire)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)