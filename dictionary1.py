band=["mel","geri","victoria","mel","emma"]
counts={}
for member in band:
    if member not in counts:
        counts[member]=1
    else:
        counts[member]+=1

for member in counts:
    print(member, counts[member]) 
