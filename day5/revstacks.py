stacks =[ ['N', 'H', 'S', 'J', 'F', 'W', 'T', 'D'],
['G', 'B', 'N', 'T', 'Q', 'P', 'R', 'H'],
['V','Q','L'],
['Q', 'R', 'W', 'S', 'B', 'N'],
['B', 'M', 'V', 'T', 'F', 'D', 'N'],
['R', 'T', 'H', 'V', 'B', 'D', 'M'],
['J', 'Q', 'B', 'D'],
['Q', 'H', 'Z', 'R', 'V', 'J', 'N', 'D'],
['S','M','H','N','B']]

for i in stacks:
    print(f"stack{stacks.index(i)+1} = ", i[::-1])
