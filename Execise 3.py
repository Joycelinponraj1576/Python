score = float(input("Enter Score: "))
if score < 0.0 or score > 1.0:
    print("It is out of range")
elif score >= 0.9:
    print("A grade")
elif score >= 0.8:
    print("B grade")
elif score >= 0.7:
    print("C grade")
elif score >= 0.6:
    print("D grade")
else:
    print("Fail")
