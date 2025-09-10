a = [0, 0, 1, 2, 3 ,4]

s = Set()
for n in a:
    if n in s:
        return False
    n.insert(n)
