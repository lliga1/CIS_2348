# Marianel Liga
# PSID 1394330
# Homework 11.22

words = input().split()
for word in words:
    count = 0
    for n in words:
        if n == word:
            count += 1
    print(word, count)