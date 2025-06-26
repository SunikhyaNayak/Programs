def fibo (n:int)->None:
    prev_of_prev=0
    prev=1
    print(prev_of_prev,end=" ")
    print(prev,end=" ")
    for i in range(1,n-1):
        cur=prev+prev_of_prev
        print(cur, end=" ")
        prev_of_prev=prev
        prev=cur
def main():
    n=int(input("Enter an integer:"))
    fibo(n)
if __name__=="__main__":
    main()
