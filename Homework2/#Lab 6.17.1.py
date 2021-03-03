#Marianel Liga 
#CIS 2348
#Lab 6.17.1
#Student ID: 1394330

user=input()
password=''
for x in user:
    if(x=='i'):
        password+="!"
    elif(x=='a'):
        password+="@"   
    elif(x=='m'):
        password+="M" 
    elif(x=='B'):
        password+="8"  
    elif(x=='o'):
        password+="."
    else:
        password+= x  

password+="q*s"
print(password) 