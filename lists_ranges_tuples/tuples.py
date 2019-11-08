welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
metallica = "Ride the Lightning", "Metallica", 1984

imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish Town Walsh")
)
print(imelda)

print(metallica)
print(metallica[0])

# tuples are immutable
# metallica[0] = "Master of Puppets"

# variable can still be assigned
imelda = imelda[0], "Imelda May", imelda[2], imelda[3]
print(imelda)

# list is mutable object
# you can change list within a tuple
metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

# unpacking the tuple
title, artist, year, songs = imelda
print(title, artist, year)
for song in songs:
    number, title = song
    print("\tTrack number: {}, Title: {}".format(number, title))


# too many values to unpack
# metallica2.append("Rock")
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)
