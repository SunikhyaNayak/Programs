def fun()->int:
    n=int(input("enter an integer"))
    sum=0
    product=1
    while n > 0:
        sum=sum +  n  % 10
        product=product * n % 10
        n=n//10
    if sum == product:
        print("The sum and product are same")
    else:
        print("The sum and product are not same")
if __name__ == "__main__":
    fun()
