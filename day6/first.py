with open("day6input.txt") as f:
    datastream = f.read()


window_size = 14

temp = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
for index,char in enumerate(datastream):

    #store the first 4 characters from this index in a buffer variable
    buffer = datastream[index:index+window_size]
    # print(buffer)

    #check if it has repeating values
    if len(buffer) == len(set(buffer)):

        #now the index + 4 is the answer
        print(buffer)
        print(index+window_size)
        exit()


'''
For the first part, window_size = 4, and window_size = 14 for the second part
'''
