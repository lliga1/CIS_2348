# Marianel Liga
# PSID 1394330
# Homework 12.9

data = input().split()
name = data[0]
while name != '-1':
    try:
        age = int(data[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))

    data = input().split()
    name = data[0]