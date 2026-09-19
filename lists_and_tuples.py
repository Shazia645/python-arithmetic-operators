# list and tuple in python
marks=[34.8,77,90,55,44,88,22,33]
print(marks)
print(type(marks))
print(marks[0])
print(marks[0:7])
print(marks[0:])
list=[2,1,4,3]
list.append(5)#add somthing at the end of list
print(list.sort())#arrange list in assanding order
print(list.sort(reverse=True))#short list in desending order
list.insert(0,8)#insert element on index(index,element)
list.pop(2)#direct index 2 sa element ko hata da ga
list.remove(1)#jaha b pahla 1 dekha usko remove kr da ga
list[0]=0
print(list)
# tuples list ka duur ka bai kah skty hai strings ur tuples immutable hota hai lakin ist mutable hai
tup=(1,2,3,4)
print(type(tup))
movies=[]
move1=input("inter the name of 1st move")
move2=input("inter the name of 2nd move")
move3=input("inter the name of 3rd move")
movies.append(move1)
movies.append(move2)
movies.append(move3)
print(movies)
names=["hhh","gg","uu"]
