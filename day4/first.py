with open("day4input.txt","r") as f:
    x = f.read().split("\n")

# print(x[:2])

def one_contains_other(range1:str,range2:str) -> bool:
    a1,b1 = range1.split("-")
    a1,b1 = int(a1),int(b1)
    a2,b2 = range2.split("-")
    a2,b2 = int(a2),int(b2)


    if a2>=a1 and b2<=b1:
        #range2 is inside range1
        return True
    elif a1>=a2 and b1<=b2:
        #range1 is inside range2
        return True
    else:
        # none are inside one another completely
        return False

duplicate_count = 0
for pair_of_ass in x[:-1]:
    # print(pair_of_ass)
    r1,r2 = pair_of_ass.split(",")
    # print(r1,r2)
    if one_contains_other(r1,r2):
        print(r1,r2)
        duplicate_count+=1

print(duplicate_count) # 536
