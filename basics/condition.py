temperature = 15
age = 22
high_income = True
good_credit = True
student: True

'1. If statement'
if temperature > 30 :
    print("it's warm")
    print("ok")
elif temperature > 20:
    print("it' nice")
else:
    print("it's cold")
print("done")


'2. ternary operator'
message = "eligible" if age >= 22 else "not eligbible"
print(message)

'3. logical operators'
if high_income and good_credit:
    print("Eligible")
else:
 print("Not Eliglible")

 '4. Chaining comparison operators'
 if 18 <= age < 65:
     print("Eligible")
