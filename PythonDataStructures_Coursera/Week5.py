"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
mydictionary = {}
for line in handle:
    fromlist = []
    fromlist = line.split()
    if len(fromlist) >= 2:
        if fromlist[0] == 'From':
            if fromlist[1] not in mydictionary:
                mydictionary.setdefault(fromlist[1], 0)
            mydictionary[fromlist[1]] = mydictionary.get(fromlist[1]) + 1
maxkey = max(mydictionary.values())
for i in mydictionary.items():
    if maxkey == i[1]:
        print('{} {}'.format(i[0], i[1]))
