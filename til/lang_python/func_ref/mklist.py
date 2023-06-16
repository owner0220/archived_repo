f=open("list.txt",'r',encoding="utf-8")
string=""
lines = f.readlines()
for line in lines:
    if "—" in line:
        string += "    - [ ]  " + line
        continue
    else:
        string += "- #### " + line
print(string)
f.close()

f=open("result.txt",'w',encoding='utf-8')
f.write(string)
f.close()