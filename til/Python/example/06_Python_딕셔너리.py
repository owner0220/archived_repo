d=dict(a=1,b=2,c=3)
print(d)
print(type(d))

color={"apple":"red", "banana":"yellow"}
print(color[apple])

for x in color.items():
    print(x)

for x in color.keys():
    print(x)

for x in color.values():
    print(x)


for k,v in color.items():
    print(k,v)

del color['apple']

print(color)