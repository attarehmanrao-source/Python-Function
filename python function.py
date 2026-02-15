#Function: def  se likha jata hai,  1 bar bana kar bar bar use kar skte hain 
#Function q use hota hai?
#1.Code short ho jata hai
#2.Time bach jata hai
#3.Program samajhna easy ho jata hai


#Q1.simple Chai Function
def chai_banao():
  
    print("aag jalao")
    print("pateli Rakho")
    print("Pani garam karo")
    print("Chai patti daalo")
    print("Cheeni daalo")
    print("Doodh daalo")
    print("Chai ready!")
chai_banao()

#Q2.Add function
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#Q3.Subraction function
def subtract(a, b):
    return a - b

result = subtract(10, 4)
print(result)

#Q4.divide function
def divide(a, b):
    return a // b

result = divide(10, 2)
print(result)

#Q5.Multiplication function
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

#Q6.Student Marksheet 
def marksheet():
    name = input("Student ka naam likho: ")
    sub1 = int(input("English marks: "))
    sub2 = int(input("Math marks: "))
    sub3 = int(input("Science marks: "))

    total = sub1 + sub2 + sub3
    average = total / 3

    print("\n----- Marksheet -----")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average:", average)

marksheet()
#Q7.Bank account
def bank_account():
    balance = 0

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose option (1-4): ")

        if choice == "1":
            amount = float(input("Deposit amount: "))
            balance += amount
            print("Amount deposited successfully.")

        elif choice == "2":
            amount = float(input("Withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance!")

        elif choice == "3":
            print("Current Balance:", balance)

        elif choice == "4":
            print("Thank you for using bank system.")
            break

        else:
            print("Invalid option!")

bank_account()