list=[10,20,30,40,50]
new_list=[]
j=0
for i in list:
    j = sum(list[0:list.index(i)+1])
    new_list.append(j)
     
print(new_list)