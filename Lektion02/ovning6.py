print("Ovning 3.2")

name = input("what is your name? ")
age =  int(input("how old are you? "))
 
if age == 1 :
 sleepTime=14
elif age == 2 :
 sleepTime=13
elif age == 3 :
  sleepTime=12
elif age == 4 :
  sleepTime=11.5
elif age in range(5, 7) :
  sleepTime=11
elif age == 7 :
  sleepTime=10.5
elif age in range(8, 11):
  sleepTime=10
elif age == 11 :
  sleepTime=9.5
elif age in range(12, 16) :
  sleepTime=9
elif age == 16 :
  sleepTime=8.5
else:
 sleepTime= 8

print(name , "needs" ,  sleepTime, "hour to sleep." )

