#exercise 4 tuples
#part 1
t=(1,)
t[-1]
x=range(100,201)
tup=tuple(x)
print(tup[0],tup[-1])

#part2

mylist=[23,"hi",2.4e-10]
for (count,item) in enumerate(mylist):
    print(count,item)

#part 3

first=mylist[0]
second=mylist[1]
third=mylist[2]
(first,middle,last)=mylist
