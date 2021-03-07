def IsLeap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    
    while True:
        try:
            year = int(input("Please enter a year: "))
            if year < 0:
                print("Please try again with valid year.")
            else:
                if IsLeap(year) == True:
                    print("It's a leap year!")
                else:
                    print("It's not a leap year."
                )
        except:
            print("Please input valid input")