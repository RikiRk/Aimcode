s=input("Enter the your word: ")
def reverse(s):
    return s[::-1]
def isPalindrome(s):
    rev=reverse(s)
    if(s==rev):
        return True 
    return False   
ans= isPalindrome(s)
if ans == 1:
    print("Yes, It's a Palindrome")
else:
    print("Not, It's a Palindrome")

