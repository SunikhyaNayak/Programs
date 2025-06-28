def grade (marks:int)->str:
    match marks//10:
        case 0|1|2:
            print("D")
        case 3|4:
             print("D")
        case 5|6:
            print("C")
        case 7|8:
            print("B")
        case 9|10:
            print("A")
grade(80)