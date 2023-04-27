import math

print("Welcome To Tip Calculator!")

bill = float(input("What was the Total Amount For The Bill? $"))
tip = int(input("What Percentage Would You Like To Tip? "))
people = int(input("How Many People Would You Like To Devide The Bill? "))

amount = (bill * ((100 + tip) / 100)) / people

print("The Final Amount To Be Paid By Every Individual Is: " + str(amount))