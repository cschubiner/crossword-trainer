import csv
from random import randint
clues = []

with open('crossworddata.csv','rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')

for row in reader:
  clues.append(row)

length = len(clues)
while True:
  randNumber = randint(1,100)
  print clues[randNumber][0]
  print str(len(clues[randNumber][1])) + ' letters'
  raw_input()
  print clues[randNumber][1]
  raw_input()
  print clues[randNumber][2]
  raw_input()
