def print_all_friends(g,start):
    qu = list()
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

def print_all_friends2(g, start):
    qu = list()
    done = set()

    qu.append((start, 0))

    done.add(start)

    while qu:
        (p , d) = qu.pop()
        print(p, d)

        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.app(x)