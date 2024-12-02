'''
Problem Statement:

Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle!
Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen’s age plus Anton’s age.
Ethan is the same age as Chen.
Your code should store each person’s age to a variable and print their names and ages at the end.
Anton is 3
Beth is 4
Chen is 5
Drew is 6
Ethan is 7


'''

age_anton: int = 21
age_beth: int = 21 + 6
age_chen: int = age_beth + 20
age_drew: int = age_chen + age_anton
age_ethan: int = age_chen

print(f"Aton is {age_anton} years old.")
print(f"Beth is {age_beth} years old.")
print(f"Chen is {age_chen} years old.")
print(f"Drew is {age_drew} years old.")
print(f"Ethan is {age_ethan} years old.")