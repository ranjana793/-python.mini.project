import os
import csv
from datetime import datetime


print("Welcom To Personal Expense Tracker")

# add espenses
def add_expenses(descroption,amount): 
#create csv file to store the expenses data    
    with open('personal_expense.csv','a' , newline='') as   file:

        line=csv.writer(file)
        line.writerow([descroption,amount,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])

    print('Expensesb Record')

# view expenses

def view_expenses():
     with open('personal_expense.csv', 'r') as file:
        expenses= csv.reader(file)
        for expenses in expenses:
            print(f' your Expenses details below \n name:{expenses[0]}, amount:{expenses[1]},date{expenses[2]}')


def main():
    while True:
        print('1. Add expenses')
        print('2. View expenses')
        print('3. Exit')

        choose=input('Please select any option from above:')

        if choose=='1':
            description=input('Please enter description:')
            amount=float(input("Please enter amount:"))

            add_expenses(description,amount)

        elif choose=='2':
            view_expenses()

        elif choose=='3':
            print('Thank you for closing the app')
            break

if __name__=='__main__':
    main()
         
         



        
               