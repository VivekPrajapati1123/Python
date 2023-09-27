set1 = {18,28,36,39,50}
n=28
for i in set1:
    if i == n:
        set1.remove(n)
        set1.add(0)
print(set1)

