tup=(1,2,3,4,5,6,7,8,9)
#op = [1,3,5,7,9,8,6,4,2]
list1=list(tup)
#print(list1)
list2 = []
l=max(list1)
#print(l)
for num in list1:
    # checking condition
    if num % 2 != 0:
        list2.append(num)
for num in list1:
    # checking condition
    if num % 2 == 0:
        list2.append(num)
for i in range(len(list2)):
    print(list2[i])
