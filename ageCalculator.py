import datetime

yearAge = int(input("Enter your year of birth:\n"))
now = datetime.datetime.now()
currentYear = now.year

#Checking input validity
def IsValidInput():
    if 0 > yearAge:
        print("Invalid input")
    elif yearAge > 125 and yearAge < 1900:
        print("You seem to be the oldest person alive!")
        exit() 
    elif yearAge > currentYear:
        print("You are not yet born!")
        exit()   
    else:
        return True

#Calculating year when age will be 100
def AgeAfter100(yearAge):
    if IsValidInput() == True:
        Age = 2020 - yearAge
        print(f"You will be 100 years old in the year {yearAge + 100}")

#Age After specified years
def AgeAfter(yearAge):
    if IsValidInput() == True:
        interestedYear = int(input("\nEnter the year you want to know your age in:\n"))
        while(interestedYear < yearAge ):
            interestedYear = int(input("Invalid input!\nEnter a year after your birth year.\n"))
        print(f"You will be {interestedYear - yearAge} year old in {interestedYear}")

AgeAfter100(yearAge)
AgeAfter(yearAge)
