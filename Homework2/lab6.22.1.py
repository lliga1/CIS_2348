#Marianel Liga 
#CIS 2348
#Lab 6.22.1
#Student ID: 1394330

input_1 =int(input()) #input coefficients

input_2=int(input())

input_12=int(input())

input_3=int(input())

input_4=int(input())

input_34=int(input())

solution = False

for x in range(-10,11): 
  for y in range(-10,11):
    if(input_1*x+input_2*y==input_12 and input_3*x+input_4*y==input_34):
      print(x,y)
      solution = True

if not solution:
  print("No solution")
     