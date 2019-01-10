import os
basicpath="./dir/"
big=""
sub=""
combb=basicpath + big
combs=basicpath + big + "/" + sub


f=open("list.txt",'r',encoding="utf-8")
string=""
lines = f.readlines()
for line in lines:
    if "—" in line:
        #하위항목
        sub = line.replace("\n","").split(" — ")[0]
        combs=basicpath + big + "/" + sub
        os.mkdir(combs)
        
        print(combs)
        # print("::::::::",line.replace("\n","").split(" — ")[0])
    else:
        #대항목
        big = line.replace(" ","_").replace("\n","")
        combb=basicpath + big
        os.mkdir(combb)
        print(combb)
        # print(line.replace(" ","_").replace("\n",""))
f.close()