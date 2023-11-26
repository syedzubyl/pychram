from datetime import date
print("Simple Age Calculator\n")
print("---------------------\n")
birthYear = int(input("Enter the birth year: "))
birthMonth = int(input("Enter the birth month: "))
birthDay = int(input("Enter the birth day: "))
print("")
dateOfBirth = date(birthYear, birthMonth, birthDay)
today = date.today()
day_check = ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
year_diff = today.year - dateOfBirth.year
age_in_years = year_diff - day_check
remaining_months = abs(today.month - dateOfBirth.month)
remaining_days = abs(today.day - dateOfBirth.day)
print("Age:", age_in_years, "Years", remaining_months, "Months and", remaining_days, "days")
age_limit = {
    "driving": 18,
    "voting": 18,
    "retirement": 60
}
for category, limit in age_limit.items():
    if age_in_years >= limit:
        print("You are eligible for", category + ".")
    else:
        print("You are not eligible for", category + ".")
print("You have to wait for", limit - age_in_years, "more years.")