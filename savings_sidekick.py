#Alanza Blake
#Citi HBCU Hackathon
#Challenge 2
#Savings Sidekick
import time#import time library

class Account:
    def __init__(self):#constructor for Account class
        self.fund = 0#initialize the emergency fund to 0 since the fund starts at 0
        self.income = 0#initialize student income
        self.expenses = 0#initialize student expenses
        self.months_left = 0#initialize months
        self.goal = 300#Give a default amount to save
        self.suggestion = 0#initialize suggested monthly amount
    def set_income(self):
        self.income = float(input("Please enter an estimate monthly income. This can include a part-time job, an allowance, gifts, etc. : "))
        print("Your income has been updated to $%.2f." % (self.income))
    def set_expenses(self):
        self.expenses = float(input("Please enter your estimated monthly expenses: "))
        print("Your expenses has been updated to $%.2f." % (self.expenses))
    def set_goal(self):
        self.goal = float(input("Please enter your goal for your emergency fund: "))
        print("Your emergency fund goal has been updated to $%.2f." % (self.goal))
    def set_months(self, total_months):#method is used to set the original amount of months so the information is in the class
        self.months_left = total_months#set the parameter to total_months
    def deduct_month(self):
        self.months_left -= 1#deduct a month as each month passes by
    def calculate(self):#the calculate method calculates the suggested amount the sidekick tells the user to put in their fund
        print("Your suggested amount is calculating...")
        time.sleep(3)#give a 3 second break
        #I'm going to calculate the suggested amount in two ways: by dividing the difference between the goal and the balance by the months left 
        #and by multiplying the difference between the income and expenses by 15%. 
        #Then I'll compare the two to see which one is more and should be added to the fund.
        self.compare1 = (self.income - self.expenses) * .15#calculate by taking 15% of the difference of the income and expenses
        if self.months_left != 0:#if there are months left
            self.compare2 = (self.goal - self.fund) / self.months_left#calculate by subtracting the goal by the fund and divide that difference by the remaining months
        else:
            self.compare2 = (self.income - self.expenses) * .15#set to default calculation if it's equal to 0
            
        if self.compare1 > self.compare2:#if the first calculation is more than the second then the first calculation is the suggested amount
            self.suggestion = self.compare1#set suggested amount to first calculation
        elif self.compare1 < self.compare2:#if the first calculation is less than the second then the second calculation is the suggested amount
            self.suggestion = self.compare2#set suggested amount to second calculation
        else:#if they're equal
            self.suggestion = self.compare1#set it to either or
        
        if self.months_left == 0:#if there are no months left
            if self.fund < self.goal:#if the user hasn't reached their goal yet
                self.suggestion = self.goal - self.fund#the suggested amount is the remaining amount
        print()#space
        print("Your suggested amount for this month is $%.2f" % (self.suggestion))#print suggested amount
    def add_to_fund(self):
        money = float(input("Please enter your monthly amount to your fund: "))
        self.fund += money#add money onto fund
        print("$%.2f added into your emergency fund." % (money))#message
        if self.fund >= self.goal:#if user has met the goal
            print("You have made your goal! Let's continue!")#message
    def menu(self):#menu to use in main
        print("1: I want to add to my fund.")
        print("2: I want to see a display of my information.")
        print("3: I want to update my income for this month.")
        print("4: I want to update my expenses for this month.")
        print("5: I want to update the emergency fund goal.")
        print("6: I'm done with this month.")
    def display_info(self):
        print("Emergency Fund Balance: $%.2f" % (self.fund))#print out current balance information
        print("Emergency Fund Goal: $%.2f" % (self.goal))#print out current goal
        print("Current Estimated Monthly Income: $%.2f" % (self.income))#print out current income information
        print("Current Estimated Monthly Expenses: $%.2f" % (self.expenses))#print out current expenses information
        print("Current Suggested Monthly Amount: $%.2f" % (self.suggestion))#print out suggested amount
        print("Months Left Until Graduation/College: %d" % (self.months_left))#print out months left
    def results(self):#method that gives user final result
        if self.fund < self.goal:#if fund is less than goal
            print("Unfortunately, you did not meet your goal for your emergency fund. You've saved $%.2f" % (self.fund))
        elif self.fund == self.goal:#if fund is equal to the goal
            print("You have met your goal exactly! You've saved $%.2f" % (self.fund))
        elif self.fund > self.goal:#if fund is more than the goal
            print("You have exceeded your goal! You've saved $%.2f" % (self.fund))
        print("You can continue to save by taking 15% of your remaining income after expenses \nor dividing your goal by the amount of months you plan to save during.")

def main():
    #Intro for the user
    print("Welcome to the Savings Sidekick!")
    print("We're here to help you create and build a emergency fund to for any college financial hardships you may face.")
    print("Let's start by entering some information about your current income, expenses, and financial goals.")
    print()#space
    
    emergency_fund = Account()#create new object of the class called emergency_fund
    
    #The user will be asked initial questions so the savings sidekick
    print("Month 1: ")
    print()#space
    print("Let's start with any income or money you're currently receiving.")
    emergency_fund.set_income()#call method from the class to get input
    print()#space
    print("Now let's talk about your expenses. Can you calculate an estimate of your monthly expenses?")
    emergency_fund.set_expenses()#call method from the class to display input for expenses
    print()#space
    option = input("Do you have a particular amount that you want to save(Yes/No)? ")#asking if user they have a particular amount they'd like to save.
    if option.lower() == "yes":#if yes then get user input
        emergency_fund.set_goal()#call method from the class to display input for goal
    elif option.lower() == "no":#keep default amount
        print()#space
        print("Okay. We're going to aim for the default amount, which is $300.")
    print()#space
    months = int(input("Lastly, How many months do you have until graduation or until you attend college? "))
    emergency_fund.set_months(months)#call method from class to set the months left
    print()#space
    emergency_fund.calculate()#call calculate method to give user their monthly suggested amount
    print("Now how much will you be adding to your emergency fund this month?")
    print("Note: It doesn't have to be the sidekick's suggestion but you may not reach your goal if it's less than.")
    print()#space
    emergency_fund.add_to_fund()#call method to add to the emergency fund
    print()#space
    emergency_fund.deduct_month()#call method to subtract a month
    emergency_fund.display_info()#call method to show all the information
    print()#space
    month_counter = 1#counter for the months
    
    #While loop to keep the program going until the months are done
    while month_counter < months:#until the month counter reaches the actual amount of months
        month_counter += 1
        emergency_fund.deduct_month()#subtract one month
        print("Month %d: " % (month_counter))#to print current month
        print()#space
        emergency_fund.calculate()#calculate for each month
        print()#space
        choice = 0#initialize choice to use in loop
        while choice != 6:#second while loop to choose the options
            emergency_fund.menu()#display menu
            choice = int(input("Please enter a choice: "))#display user input
            print()#space
            if choice == 1:#add to fund
                print("Note: Skipping for the month means you may not reach your goal or your suggested amount may increase.")
                emergency_fund.add_to_fund()#call add to fund
            elif choice == 2:#display info
                emergency_fund.display_info()#call display information
            elif choice == 3:#update income
                emergency_fund.set_income()#call set income method to so the user can provide a new income
                emergency_fund.calculate()#recalculate
            elif choice == 4:#update expenses
                emergency_fund.set_expenses()#call set expenses to so the user can enter the expenses
                emergency_fund.calculate()#recalculate
            elif choice == 5:#update the goal
                emergency_fund.set_goal()#reset the goal
                emergency_fund.calculate()#recalculate
            print()#space
    emergency_fund.results()#call method to show the final results

main()#call main function

