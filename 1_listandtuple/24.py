#sum , avg

'''def avg1(*num):
    avg1 = (sum(num))/ (len(num))
    print(avg1)

def sum1(*num):
    sum1 = sum(num)
    print(sum1)

def minmax(*num):
    print(min(*num))
    print(max(*num))

avg1(23,33,4)
sum1(134,56)
minmax(12345,8765432,456789,2345678)'''

def stu(**values):
    for key,value in values.items():
        print (key,value)

stu(name="ps",marks=89)
