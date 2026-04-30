a=[chr(i) for i in range(65,91)]
print(a)

a=[chr(i) for i in range(65,91) if chr(i) not in "AEIOU"]
print(a)

a=6789
b=[int(i) for i in str(a)]
print(max(b))
