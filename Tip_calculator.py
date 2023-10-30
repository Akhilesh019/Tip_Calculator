print("Welcome to the tip calculator")
bill = input("What was the total bill?\n")
percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("how many people to split the bill?\n")

percentage_1 = float(bill)*int(percentage)/100
total_bill = float(bill) + float(percentage_1)
share = round(float(total_bill)/int(people), 2)
share_1 = "{:.2f}".format(share)

print("Each person should pay: " + str(share_1))
