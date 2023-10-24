def palindrome(n):
    odd = 0
    for i, c in enumerate(n):
        if c != n[~i]:
            odd += 1
    if odd % 2 == 1:
        half = odd // 2
        pal = " ".join((n[i] if i < half else n[~i] for i in range(len(n))))
        return pal
    else:
        half = odd // 2
        pal = " ".join((n[i] if i <= half else n[~i] for i in range(len(n))))
        return pal
n = input("Enter the number:")                                
print(palindrome(n))