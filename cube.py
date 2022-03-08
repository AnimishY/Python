L = [1,2,3]
output = list()

for i in L:
    res = [(i, pow(i, 3))]
    output = output + res

print(output)