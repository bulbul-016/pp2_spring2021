list1=[2, 3, 5, 16, 100]
list2=list(filter(lambda x: x%2==0,list1))

print(list2)

#[2, 16, 100]