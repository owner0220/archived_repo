a=1.2
print(id(a))

a=2.3
print(id(a))

def change(x):
    x[0]='H'

wordlist=['j','a','m']

change(wordlist)
print(wordlist)


def change(x):
    x=x[:]
    x[0]='h'
    return None

wordlist=['j','a','m']

change(wordlist)

print(wordlist)