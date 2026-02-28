'''write a program to check whether a string is palindrome or not
-input -Madam
exected output-string is palindrome'''

string='Madam'
string=string.lower()
s=string[::-1]
if(s==string):
    print("String is Palindrome")
else:
    print("String is not Palindrome")