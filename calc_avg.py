def avg(a: list)->float:
    sum=0
    #for i in range(0,len(a)):
    for n in a:
        sum = sum + n
    return sum/len(a)

def main():
    nums=[2,3,7,9,11]
    print ("Orginal number")
    #print (nums)
    for n in nums:
        print(n, end=" ")
    print()
    print(f"\naverage is {avg(nums)}")
    print()
if __name__ == "__main__":
    main()


   