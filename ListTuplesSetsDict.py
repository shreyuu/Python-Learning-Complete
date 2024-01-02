# <---LIST--->
l = [40, 20, 10, 30]
l.sort(); print(l)
l.reverse(); print(l)
l.append(50); print(l)
l.remove(20); print(l)
l.pop(); print(l)

# <---TUPLES--->
t = (40, 20, 10, 30, 40)
a= t.count(40); print(a)

# <---SETS--->
a={"red","green","blue"}
b={"cyan","magenta","yellow"}
c=a.union(b); print(c)
c=a.difference(b); print(c)


# <---DICT--->
a={1:"red",2:"green",3:"green"}
b=a.fromkeys([1,2,3]); print(b)
c=a.items(); print(c)