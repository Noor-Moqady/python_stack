for x in range(0, 151, 1):
    print (x)


for y in range(5, 1001, 5):
    print (y)

for z in range(1, 101):

 
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print (z)

sum = 0
for n in range(500001):
    if n % 2 != 0:
        sum += n
print(sum)


for f in range(2018, 0 , -4):
    print(f)



lownum= 1
highnum = 100
mult = 2
for z in range(lownum, highnum+1, 1):
    if z % mult == 0:
        print(z)