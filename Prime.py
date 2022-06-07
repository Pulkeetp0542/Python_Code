a=int(input("Enter the number"))
if a>1:
    for x in range(2,a):
        if (a%x==0):
            print("Number is not Prime")
            break
        else:
            print("Number is Prime")
            break
else:
    print("Prime")