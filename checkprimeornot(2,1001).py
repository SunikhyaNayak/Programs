def all_prime()->None:
    for n in range (2,1001):
        for i in range(2,n//2+1):
            if n%i==0:
                break
            else:
                print(n,end=" ")
def main():
    all_prime()
if __name__ == "__main__":
    main()
    

    