def palindrome(x):
    if x<0:
        return False
    s=str(x)
    return s==s[::-1]
x=-45
print(palindrome(x))