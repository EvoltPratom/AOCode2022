stacks = [['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N'],
    ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G'],
    ['L', 'Q', 'V'],
    ['N', 'B', 'S', 'W', 'R', 'Q'],
    ['N', 'D', 'F', 'T', 'V', 'M', 'B'],
    ['M', 'D', 'B', 'V', 'H', 'T', 'R'],
    ['D', 'B', 'Q', 'J'],
    ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q'],
    ['B', 'N', 'H', 'M', 'S']]


# print(stacks)
with open("day5input.txt","r") as f:
    x = f.read().split("\n")

# print(x[:2])
def move_from(s1:list,s2:list):
    #moves the top of stack from s1 to s2
    x = s1.pop()
    s2.append(x)


for i in x[:-1]:
    '''
    i = move 3 from 1 to 2

    for _ in range(3):
        move_from(stacks[1-1],stacks[2-1])
    '''
    aa = i.split(" ")
    range_val,s1_val,s2_val = int(aa[1]),int(aa[3])-1,int(aa[5])-1
    print(range_val,s1_val,s2_val)
    for _ in range(range_val):
        move_from(stacks[s1_val],stacks[s2_val])


for cr in stacks:
    print(cr[-1],end="")
print()
