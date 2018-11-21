#ex5 part 2
with open ("weather.csv","r") as reader:
    line=reader.readline()


    count=0

    while line !='':
        print(line)
        line=reader.readline()

    print("It's over")
