list=[]
for value in range(1,1001):
    if value % 2 == 0 or value % 3 == 0 or value % 5 == 0:
        list.append(value)
#print(list)
sum_of_values = sum(list)
print(sum_of_values)

type(sum_of_values)
