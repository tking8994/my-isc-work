#python exercise 3 part 1
x=[1,2,3,4,5]
print(x)
print(x[1])
print(x[-2])
print(x[:])
print(x[0:4])
#part 2
y=list(range(1,11))
print(y)
y[0]=10
y.append(11)
y.extend([12,13,14])
print(y)

#part 3

forward=[]
backwards=[]
values=["a","b","c"]
for x in values:
    forward.append(x)
    backwards.insert(0,x)

print("forward is:", forward)
print("backward is:", backwards)
forward.reverse()
forward==backwards

#part 4
countries=["uk","usa","uk","uae"]
dir(countries)
countries.count("uk")





