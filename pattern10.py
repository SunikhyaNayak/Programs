def pattern ()->None:
    for i in range(0,5):
        for j in range(1,6):
            print((i+j),end=" ")
        print()
def main():
    pattern()
if __name__ == "__main__":
    main()