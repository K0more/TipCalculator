a = int(input("Enter the total amount of bill you had "))
z = int(input("Enter the percentage of tip you would like to give "))
b = (a/100)*z
c = int(input("Enter the number of people the tip is to be divided to "))
d = b/c
e = int(input("How many people are splitting the bill "))
g = a/e
tip = str(d)
print("The tip should be " + tip + " dollars each.")
print(f"Each person should pay {g} dollars.")
