stacks = [['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N'],
    ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G'],
    ['L', 'Q', 'V'],
    ['N', 'B', 'S', 'W', 'R', 'Q'],
    ['N', 'D', 'F', 'T', 'V', 'M', 'B'],
    ['M', 'D', 'B', 'V', 'H', 'T', 'R'],
    ['D', 'B', 'Q', 'J'],
    ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q'],
    ['B', 'N', 'H', 'M', 'S']]

with open("day5input.txt","r") as f:
    x = f.read().split("\n")

def move_from(no_of_crates:int,s1:list,s2:list) -> list:
    '''
    temp = s1[-no_of_crates:]
    s1 = s1[:-no_of_crates]
    s2 = s2+temp
    '''
    temp = s1[-no_of_crates:]
    s1 = s1[:-no_of_crates]
    s2 = s2+temp
    print(s1)
    print(s2)
    print()
    return [s1,s2] # i would ideally like to not return anything



# stacks[0],stacks[1] = move_from(3,stacks[0],stacks[1])
# stacks[6],stacks[0] = move_from(1,stacks[6],stacks[0])
# print(stacks[0],stacks[1])
# print(stacks[6],stacks[0])
for i in x[:-1]:
    print(i)
    aa = i.split(" ")
    no_of_crates,s1_val,s2_val = int(aa[1]),int(aa[3])-1,int(aa[5])-1
    stacks[s1_val],stacks[s2_val] = move_from(no_of_crates,stacks[s1_val],stacks[s2_val])
    # print(no_of_crates,s1_val,s2_val)


for cr in stacks:
    print(cr[-1],end="")
print()
