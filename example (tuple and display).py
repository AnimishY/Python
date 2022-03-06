st = ((101, 'Alpha', 98), (102, 'Bravo', 95), (103, 'Charl', 97), (104, 'Delta', 87))

print('Serial Number', 'Roll Number', 'Name', 'Marks')
for i in range (0, len(st)):
    print((i+1), '\t', st[i][0], '\t', st[i][1], '\t', st[i][2])