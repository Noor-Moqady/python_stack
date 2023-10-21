def countdown (num):
    numlist1 = []
    for i in range(num,-1,-1):
            numlist1.append(i)
    print (numlist1)
    return numlist1
countdown(5)
countdown(10)
countdown(20)



numlist2 = [1,2]
def print_return (numlist2):
    print (numlist2[0])
    return numlist2 [1]
print_return(numlist2)
print(print_return(numlist2))

 
numlist3 = [1,2,3,4,5]
def pluslength (numlist3):
    return  numlist3[0] + len(numlist3)
print(pluslength(numlist3))


numlist4 = [5,2,3,2,1,4]
def greaterthan_second(numlist5):
    numlist5 = []
    for i in range(0,len(numlist4),1):
        if numlist4[i] > numlist4[1]:
            numlist5.append(numlist4[i])
    return numlist5
print(greaterthan_second(numlist4))


def x(lenght,value):
    numlist6 = []
    for i in range(0,lenght, 1):
        numlist6.append(value)
    return numlist6
print (x(4,7))