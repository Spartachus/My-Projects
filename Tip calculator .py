print("Welcome to the Tip calculator")
Total_bill=float(input("What was the total bill:£"))
tip=float(input("How much would you like to give:%"))
num_client=float(input("How many people are you:"))
total_tip=(tip/100)*Total_bill
new_bill=Total_bill+total_tip
all=new_bill/num_client
#The thing in the semi backets round it to the second decimal place
print(f"You will give £{total_tip} to the server")
print(f"You have to all pay £{all:.2f} each")
