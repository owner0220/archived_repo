colors=['red','green','gold']
print(colors)
print(type(colors))


colors.append('blue')
print(colors)

colors.insert(1,'black')
print(colors)

print(colors.index('red'))

colors += ['red']
print(colors)

colors +='red'
print(colors)

print(colors.count('red'))

colors.pop()

print(colors)

colors.remove('gold')
colors.sort()
print(colors)

colors.reverse()
print(colors)