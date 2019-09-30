a = open("./insultes.txt").readlines()

b = list(set(a))

for l in b:
    print(l)
