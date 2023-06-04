# Problem 1 (a)

'''
file = open("text1.txt", encoding="latin-1").read().split()

word_count = {}
word = []
repetition = []
repeat = 0
counter = 0

for i in range (len(file)):

    for k in range (0, i):

        if file[i] == file[k]:
            repeat += 1

    if  repeat == 0:

        word.append(file[i])

        for j in range (len(file)):
            if file[i] == file[j]:
                counter += 1

        repetition.append(counter)


    repeat = 0
    counter = 0


for i in range (len(word)):
        word_count[word[i]] = repetition[i]

print(word_count)





# Problem 1 (b)

integer = [0] * 100

for i in range (1, 101):
    integer[i-1] = i

def top10 (L):

    top10 = [0] * 10

    for i in range (0, 10):

        top10[i] = max(L)
        L.remove(max(L))

    return top10


print(top10(integer))





# Problem 1 (c)

file = open("1342-0.txt", encoding="latin-1").read().split()

word_count = {}
frequency = {}
word = []
repetition = []
repeat = 0
counter = 0

for i in range (len(file)):

    for k in range (0, i):

        if file[i] == file[k]:
            repeat += 1

    if  repeat == 0:

        word.append(file[i])

        for j in range (len(file)):
            if file[i] == file[j]:
                counter += 1

        repetition.append(counter)


    repeat = 0
    counter = 0


for i in range (len(word)):
        word_count[word[i]] = repetition[i]



def top10 (L):

    top10 = [0] * 10

    for i in range (0, 10):

        top10[i] = max(L)
        L.remove(max(L))

    return top10


for i in range (0, 10):
        frequency[repetition[i]] = word[i]

print(frequency)
'''

















