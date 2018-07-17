# q3
# In a certain shop, taxes are impossed basing on the amount of cash spent.
# Using the table below, print out the total cash spent for customers who bought good worth
#  the following amounts
# 1. sh 2500
# 2. sh 10000
# 3. sh 25000
# 4. sh 70000

print("Enter amount of cash spent")
cash=int(input("cash:"))
if cash<=1000:
    print("Amount of tax is: sh 100\n")
elif cash>1000 and cash<=5000:
    print("Amount of tax is : 250 \n")
elif cash>5000 and cash<=15000:
    print("Amount of tax is : 300 \n")
elif cash>15000 and cash<=30000:
    print("Amount of tax is : 400 \n")
elif cash>30000:
    print("Amount of tax is : 500\n")
print("Thank you for shopping with us\n"
      "___COME AGAIN____")