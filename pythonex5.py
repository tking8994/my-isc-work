#exercise 5
#writer.write -wrrites a single string
#writer.writelines wirghts a list of strings
#need to write newline characters use \n at end of each component

with open ('weather.csv',"r") as reader:
    data=reader.read()

print(data)
