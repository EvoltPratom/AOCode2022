with open("day4input.txt","r") as f:
    x = f.read().split("\n")

# print(x[:2])
def one_overlaps_other(range1:str,range2:str) -> bool:
    a1,b1 = range1.split("-")
    a1,b1 = int(a1),int(b1)
    a2,b2 = range2.split("-")
    a2,b2 = int(a2),int(b2)

    #check if range1 overlaps range2
    if a1<=a2 and a2<=b1:
        #overlap
        return True
    elif a2<=a1 and a1<=b2:
        return True
    return False

overlap_count = 0
for pair_of_ass in x[:-1]:
    # print(pair_of_ass)
    r1,r2 = pair_of_ass.split(",")
    # print(r1,r2)
    if one_overlaps_other(r1,r2):
        print(r1,r2)
        overlap_count+=1

print(overlap_count) # 845
# print(one_overlaps_other("2-4","6-8")) # returns False
