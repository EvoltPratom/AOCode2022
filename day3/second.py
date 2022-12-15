ascii_letters = ["",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority = ascii_letters.index

def common_letter_betn_str(str1,str2,str3):
    str1.strip()
    str2.strip()
    str3.strip()

    cur_priority = 0
    for i in ascii_letters:
        if i in str1 and i in str2 and i in str3:
            t_p = priority(i)
            if t_p > cur_priority:
                cur_priority = t_p

    return cur_priority#, ascii_letters[cur_priority]


with open("input.txt","r") as f:
    x = f.readlines()

# print(x[0::3])
count = 3
list_of_threes = []
for i,j in enumerate(x):
    j.strip()
    if count==3:
        count = 0
        list_of_threes.append([])

    list_of_threes[len(list_of_threes)-1].append(j)
    count+=1

# xx = list_of_threes[2]

# print(common_letter_betn_str(*xx))

tot_pri = 0
for i in list_of_threes:
    tot_pri+=common_letter_betn_str(*i)


print(tot_pri)
