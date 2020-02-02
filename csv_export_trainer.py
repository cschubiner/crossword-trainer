import csv
import random
from collections import namedtuple

# DAYS_TO_INCLUDE = ['Sat', 'Sun', 'Fri']
random.seed(a='1', version=2)
DAYS_TO_INCLUDE = ['Sat']

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


n = 2000
chunked_clues = [clues[i * n:(i + 1) * n] for i in range((len(clues) + n - 1) // n )]

for j, clues in enumerate(chunked_clues):
  random.shuffle(clues)
  n = 500
  inner_chunked_clues = [clues[i * n:(i + 1) * n] for i in range((len(clues) + n - 1) // n )]
  for i, clues in enumerate(inner_chunked_clues):
    with open(f'output/output_trainer_{j}_{i}.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in clues:
          spamwriter.writerow([row.clue + '.   \t\t' + str(len(row.word)) + ' letters', row.word + '.    \t' + row.explanation])
    with open(f'output/letter_trainer_{j}_{i}.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in clues:
          randAnswer = row.word.replace(" ", "").replace("-", "").replace("'", "").replace("!", " ")
          lenRandAnswer = len(randAnswer)
          randLetter = random.randint(0,lenRandAnswer-1)
          answerList = list(randAnswer)
          answerList[randLetter]='_'
          output = "".join(answerList)
          arr = [output, row.word + '.    \t' + row.explanation]
          # print(arr)
          spamwriter.writerow(arr)
