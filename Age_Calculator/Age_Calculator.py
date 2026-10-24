from datetime import date

print("===== AGE CALCULATOR =====")

birth_year = int(input("Enter your birth year: "))

current_year = date.today().year

age = current_year - birth_year

print("Your age is approximately:", age, "years")
