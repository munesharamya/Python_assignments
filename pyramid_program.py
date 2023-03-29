number = (1,2,3,4,5,6,7,8,9,10)
#output = [1,3,5,7,9,8,6,4,2]
num1=list(number)
num2=len(num1)
l1=[]
for i in range(1,num2):
    if i%2!=0:
        l1.append(i)
for j in range(num2-1, 0, -1):
        if j % 2 == 0:
            l1.append(j)
for num in range(num2):
    numbers = list(map(int, input(l1).split()))
    print(numbers)













