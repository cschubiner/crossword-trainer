import csv
import random
from collections import namedtuple

random.seed(a='1', version=2)
DAYS_TO_INCLUDE = ['Sat', 'Sun', 'Fri']
START_INDEX = 0
NUM_CLUES = 3

clues = []


Row = namedtuple('Row', ['year', 'weekday', 'clue', 'word', 'total', 'explanation'])

with open('crossworddata.csv','r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader)

  for row in reader:
    year, weekday, clue,word,total, explanation = row
    clues.append(Row(
      year=year,
      weekday=weekday,
      clue=clue,
      word=word,
      total=total,
      explanation=explanation,
    ))

random.shuffle(clues)
clues = [x for x in clues if x.weekday in DAYS_TO_INCLUDE][START_INDEX:START_INDEX + NUM_CLUES]

while True:
  randNumber = random.randint(0,len(clues) - 1)
  clue = clues[randNumber]
  print (str(len(clue.word)) + ' letters.', clue.clue)
  input()
  print (clue.word)
  input()
  print (clue.explanation)
  input()
