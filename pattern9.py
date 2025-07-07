def pattern ()->None:
    for i in range(1,6):
        for j in range(1,6):
            if i==1:
                print('1',end=" ")
            elif j<i:
                print ('0',end=" ")
            else:
                print('1',end=" ")
        print()
def main():
    pattern()
if __name__ == "__main__":
    main()