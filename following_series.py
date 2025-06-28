def ser1(n:int)->None:
    x=0
    for i in range(1,n+1):
        x=x+(i*i)
        print(x,end=" ")
def main():
    n=int(input("Enter an integer:"))
    ser (n)
if __name__== "__main__":
    main()