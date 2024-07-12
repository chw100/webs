from datetime import date

def calculate_age(dob):
    today = date.today()

    #calculate years of age
    age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    #calculate age in months
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age_months = (12 - dob.month) + today.month - 1
    else:
        age_months = today.month - dob.month
    
    #calcuate age in days
    if today.day < dob.day:
        #go back one month to get the correct number of days in the previous month
        month_back = (today.month - 1) if today.month > 1 else 12
        month_days = (date(today.year, today.month, 1) - date(today.year, month_back, 1)).days
        age_days = month_days - (dob.day - today.day)
    else:
        age_days = today.day - dob.day

    return age_years, age_months, age_days

def main():
    #Take user input
    dob_str = input("Enter your birthdate (YYYY-MM-DD): ")
    year, month, day = map(int, dob_str.split('-'))
    dob = date(year, month, day)
    #calculate age
    age_years, age_months, age_days = calculate_age(dob)

    #Result
    print(f"You are {age_years} years, {age_months} months and {age_days} days old.")

if __name__ == "__main__":
    main()