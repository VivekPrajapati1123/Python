def decimal(n,shift):
    s = str(n)
    if shift > len(s):
        return d[::-1]
    return s[shift:] + s[:shift]
n = 12345
shift = int(input("Enter the shift number:"))
print(decimal(n,shift))