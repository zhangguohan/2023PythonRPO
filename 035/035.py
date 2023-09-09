print("welcome to the rollercoaster!")
height = int(input("what is yout hegigi in cm:"))
#age = int(input("what is yout age in :"))
bill = 0
#
if height > 120:
     print("you >>120")
     age = int(input("input age "))
     if age <=12:
          bill +=5124

          print(f"heiger > 120 and age >=12：{bill}")

     elif age<=18:
          bill +=7
          print(f"heige>120 age 12--18 :{bill}")

     elif age>45 and age <55:
         print(f"heige>120  free ")
     else:
         bill += 12
         print(f"heige>120 age 12--18 :{bill}")
     wants_photo = input("Do you want photo? Y and N")
     if wants_photo =="Y":
         bill +=3
         print(f"heige>120 age 12--18 :{bill}")
else:
     print("you bit 18")
