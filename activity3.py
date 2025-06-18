h=float(input("Enter your height:"))
w=float(input("Enter your weight:"))

bmi=w/(h/100)**2
print("your bmi is:",bmi)

if bmi<15:
    print("You are underweighted")
elif bmi<25:
    print("You are healthy")
elif bmi>25:
    print("You are overweighted")
else:
    print("Go to hospital")