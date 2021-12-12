
# print("Here you can check if any phrase you input can be composed out of the other one, by writting down two.")

# while True:
   
#  input1 = (input('Input your first phrase: ').upper())
#  input2 = (input('Input your second phrase: ').upper())

#  phrase1 = set()
#  phrase2 = set()

#  for element in input1: 
#     if element.isalpha():
#         phrase1.add(element)


#  for element in input2: 
#      if element.isalpha():
#         phrase2.add(element)

#  print('Letters from the first phrase: ', phrase1)
#  print('Letters from the second phrase: ', phrase2)

 



#  if phrase1.issuperset(phrase2):
#         print("Using this two you can form one from another")
#  else:
#         print("Using this two you cannot form one from another")


#  answer= input('Do you want to do that again? If you do, type Yes, and if not, type No:  ')
#  if answer == "Yes":
#         continue
#  elif answer== "No":
#         break

# print('Goodbye')

# a = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2,
#      'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
#      'Q': 1, 'Z': 1}

# letter = (input("Введіть слово/слова: ").upper()).split()
# result = []
# for i in range(len(letter)):
#     score = 0
#     for j in letter[i]:
#         if j in a:
#             score += a[j]
#     result += [score]

# print(result)

word = (input('Input some words: ').upper())

l = {'A':1,'E':1,'I':1,'L':1,'N':1,'O':1,'R':1,'S':1,'T':1,'U':1,
        'D':2,'G':2,
        'B':3,'C':3,'M':3,'P':3,
        'F':4,'H':4,'V':4,'W':4,'Y':4,
        'K':5,
        'J':8,'X':8,
        'Q':10,'Z':10}

word_1 = word.split()

p_all =[]
p = 0

for i in range(len(word_1)):
    for letter in word_1[i]:
        if letter in l:
            p += l[letter]
    p_all += [p]

print(p_all)



