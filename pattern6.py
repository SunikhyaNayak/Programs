def pattern()->None:
    for i in range(1,6):
        for j in range(1,6):
            if i==1 or i==5 or j==1 or j==5:
                print(1,end="")
            else:
                print(0,end="")
        print()
def main():
    pattern()
if __name__ == "__main__":
    main()
   

