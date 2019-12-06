# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#     # print(line)
#
# jabber.close()

# don't need close when using with
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "jabberwock" in line.lower():
            print(line, end='')

print("=" * 40)

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print("=" * 40)

# puts text into list
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
