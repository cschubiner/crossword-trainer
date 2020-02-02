import csv
from random import randint
clues = []
with open('crossworddata.csv','rb') as csvfile:
 reader = csv.reader(csvfile, delimiter=',')
 for row in reader:
  clues.append(row)

length = len(clues)
while True:
 randNumber = randint(0,length)
 randWord = clues[randNumber][1]
 randAnswer = randWord.replace(" ", "").replace("-", "").replace("'", "").replace("!", "")

 lenRandAnswer = len(randAnswer)
 randLetter = randint(0,lenRandAnswer-1)

 answerList = list(randAnswer)
 answerList[randLetter]='?'

 output = "".join(answerList)
print output
 raw_input()
 print clues[randNumber][0]
 raw_input()
 print clues[randNumber][1]
 raw_input()
 print clues[randNumber][2]
 raw_input()
