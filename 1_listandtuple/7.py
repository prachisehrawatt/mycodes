temps = [20, 22, 21, 24, 35, 23, 22, 24, 25, 20, 19, 30, 21, 22, 20]

lst=[20, 22, 21]

a_temp=[]

avg=int((lst[0]+lst[1]+lst[2])/3)

for i in range(3,len(temps)):
    if -4<= avg-temps[i] <=4:
        #print(lst)
        lst.pop(0)
        lst.append(temps[i])
    else:
        a_temp.append((i,temps[i]))
    
print(a_temp)