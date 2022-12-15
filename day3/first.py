from collections import Counter

ascii_letters = ["",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority = ascii_letters.index

def halves(x: str) -> list:
    x = x.strip()
    mid = len(x)//2
    return [x[:mid],x[mid:]]

def common_letter_betn_str(str1,str2):
    cur_priority = 0
    for i in ascii_letters:
        if i in str1 and i in str2:
            t_p = priority(i)
            if t_p > cur_priority:
                cur_priority = t_p

    return cur_priority#, ascii_letters[cur_priority]

with open("input.txt","r") as f:
    x = f.readlines()

x = list(map(halves,x))

# print(common_letter_betn_str(*x[2]))
tot_pri = 0
for i in x:
    tot_pri+=common_letter_betn_str(*i)

print(tot_pri)
