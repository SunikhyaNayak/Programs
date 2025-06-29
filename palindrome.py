def is_palindrome(n:int)->bool:
    rev=0
    temp = n
    while n>0:
        rev=rev*10+n%10
        n=n//10
    if temp==rev:
        return True
    else:
        return False

def main():
    num=int(input("Enter an integer:"))
    if is_palindrome(num) == True:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

if __name__ == "__main__":
    main()