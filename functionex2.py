import math

def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int,float):
        print("Bad Argument")
        return(False)
    else:
        if a <=0 or b <=0:
            print("Bad Argument")
            return(False)
    hypo = math.sqrt(a**2 + b**2)
    return hypo

a=float(input("What is A?:"))

b=float(input("What is B?:"))

print(int(calc_hypo(a,b)))
