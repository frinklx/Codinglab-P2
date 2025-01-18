s = "hello world"

print(s[4])
print(s[2:6])


# looping through each char of string
for char in s:
    print(char)
    
# looping using indeex
for index in range(len(s)):
    print(index, s[index])