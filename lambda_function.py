def function(n):
    return lambda x : x * n
doubler = function(2)
tripler = function(3)
print(doubler(10))
print(tripler(20))