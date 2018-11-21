#exercise5 part 3
with open ("weather.csv","r") as reader:
    headline=reader.readline()
    rain=[]
    for line in reader.readlines():
        print(line)
        x=line.strip().split(",")[-1]
        x=float(x)
        rain.append(x)
        



    print(rain)
    print("It's over")

with open("rain.txt","w") as writer:
    writer.writelines(str(rain))
