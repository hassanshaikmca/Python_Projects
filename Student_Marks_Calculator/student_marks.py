print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

Python = int(input("Enter Python marks: "))
SQL = int(input("Enter SQL marks: "))
Excel = int(input("Enter Excel marks: "))
Numpy = int(input("Enter Numpy marks: "))
Pandas = int(input("Enter Pandas marks: "))

total = python + sql + excel

average = total / 3

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)