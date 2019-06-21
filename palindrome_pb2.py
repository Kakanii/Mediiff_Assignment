# approach-1
def palindrome(input_string):
    input_string = input_string.upper()
    rev = input_string[::-1]
    if rev == input_string:
        print("The string you've entered is palindrome")
    else :
        print("Not palindrome")
print(palindrome(input("please enter any string to check palindrome : ")))


# approach-2
# def is_palindrome(n):
#    n = n.upper()
#    m = int(len(n)/2)
#    for i in range(m):
#       j = i + 1
#       if n[i] != n[-j]:
#          return False
#    return True
# print(is_palindrome('malayayalaM'))