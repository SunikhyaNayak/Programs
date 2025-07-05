def pattern()->None:
    for i in range(1,6):
        for j in range(1,6):
            if (i+j) % 2==0:
                print(0,end="")
            else:
                print(1,end="")
        print()
def main():
    pattern()
if __name__ == "__main__":
    main()
   

