def longest_length(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if len(i)>max1:
            max1=len(i)
            temp=i
    print("the word with longest length is :",temp ,"and length is",max1)
a=['hello','bi','hi','morning']
longest_length(a)