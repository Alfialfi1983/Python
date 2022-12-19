def fibanocci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        for i in range(n):
            print(a)
            c=a+b
            a=b
            b=c
num=int(input("enter the number:"))
fibanocci(num)