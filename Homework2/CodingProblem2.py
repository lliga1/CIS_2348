#Marianel Liga 
#CIS 2348
#Coding Problem 2
#Student ID: 1394330

def find(date_):
   mon_to_num = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   try:
      yy = date_.split(",")[-1].strip()
      month = date_.split(",")[0].split()[0]
      dd = date_.split(",")[0].split()[-1] 
      mm = mon_to_num[month]
      int(yy)
      int(dd)
      return str(mm)+"/"+dd+"/"+yy
   except:
      return ""

with open("inputDates.txt") as a: 
   for x in a.readlines():
      if x.strip() != "-1": 
         res = find(x.strip())
         if res != "":
            with open("parsedDates.txt","a+") as b:
               b.write(res+"\n")