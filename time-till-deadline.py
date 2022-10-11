from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n Example: learn python:10.02.2021\n")
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.today()
time_till = deadline_date - today_date

# calculate how many days left till deadline
print(f"Dear user, time remaining for your goal: {goal} is {time_till.days} days")



