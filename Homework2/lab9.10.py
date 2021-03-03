#Marianel Liga 
#CIS 2348
#Lab 9.10
#Student ID: 1394330

import csv

file_name = input()
words_frequency = {}

with open(file_name, 'r') as csvfile:
   csvreader = csv.reader(csvfile)
   for row in csvreader:
       for word in row:
           if word not in words_frequency.keys():
               words_frequency[word] = 1
           else:
               words_frequency[word] += 1

for key in words_frequency.keys():
   print(key + " " + str(words_frequency[key]))   


