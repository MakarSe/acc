f1 = open("Readme.txt", "r")
v = "aeiou"
m = ""
for i in f1.readlines():
    for j in i:
        if j in v:
            m += j



print(m)