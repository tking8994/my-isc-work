import sys

data={}



def split_and_strip(line):
    values=[]

    for value in line.split(","):
        values.append(value.strip())
    return values


def read_data_files(fpath):
#main code

data={}

with open(fpath,'r') as reader:

#read header

    header=reader.readline()
    col_names=split_and_strip(header)

#set up dictionary for loading

    for col in col_names:
        data[col]=[]

#read data

    for line line in reader:
    row=split_and_strip(line)
    print(f"[INFO] Data items:
         {data_items})

    
    for (index,item) in enumerate(data_items):
        col=col_names[index]
        value=item
        data[col].append(value)

return values
print(data)


if name == "main":
    args=sys.argv[1:]

    for args in args:

        print("[INFO] Reading from: {}".format(arg))
        data=read_data_file(arg)
        print(data)
    
    



  
