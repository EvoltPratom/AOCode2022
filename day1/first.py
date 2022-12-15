with open ("input.txt","r") as f:
    x = f.read()
x = x.split("\n\n")

# print(x[-1])
# y = x[len(x)-1].rstrip().split("\n")
# y = list(map(int,y))

# print(sum(y))

outp = []
for i in x[:-2]:
    y = i.rstrip().split("\n")
    y = list(map(int,y))
    outp.append(sum(y))


f1,i1 = max(outp),outp.index(max(outp))
outp.pop(i1)
f2,i2 = max(outp),outp.index(max(outp))
outp.pop(i2)
f3,i3 = max(outp),outp.index(max(outp))
outp.pop(i3)

print(f1+f2+f3)


