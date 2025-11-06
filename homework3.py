import random

# task 1

print("that program will help you to shcedule your day of tasks \n ")

# task 2

tasks = []

while True:
    task = input("Enter a study task (or press Enter to stop): \n")

    if task == "":
        break
    if task in tasks:
        print("You already added this task\n")
        continue
    tasks.append(task)


# task 3
for numbers in enumerate(tasks, start=1):
    print(numbers)


# task 4

total_tasks = len(tasks)


while True:
    question = input("\nHow many tasks do you plan to complete today? ")
    if not question.isdigit():
        continue
    question = int(question)

    if question < 1 or question > total_tasks:
        print(f"Please choose between 1 and {total_tasks}.")
        continue
    break

print(f"\nyou will complete {question} tasks today")

# task 5 

todays_tasks = tasks[:question]
total_minutes = 0

for task in todays_tasks:
    minutes = -1
    while minutes < 0:
        minutes_input = input(f"\nHow many minutes for '{task}'? ")

        if not minutes_input.isdigit():
            print("Please enter a valid number!")
            continue
        
        minutes = int(minutes_input)

        if minutes < 0:
            print("Minutes cannot be negative!")
            continue
    total_minutes += minutes

print(f"\nTotal time of studies are : {total_minutes} minutes")

# task 6 

average_minutes = total_minutes / len(todays_tasks)

average_minutes = round(average_minutes, 1)

print(f"\nAverage minutes per task: {average_minutes}")

if total_minutes < 60:
    print("\nYour plan is light.")
elif 60 <= total_minutes < 150:
    print("\nYour plan is moderate.")
else:
    print("\nYour plan is intensive.")

# bonus tasks

random.shuffle(todays_tasks)

print("\nsuggested study order: ")

for i, tasks in enumerate(todays_tasks, start=1):
    print(i,tasks)

print("\nGreat momentum!" if average_minutes >= 30 else "\nKeep going, you can do more!") 



secret = 40

low = 1
high = 40
attempts = 0

while True:
    guess = random.randint(low, high)
    print(f"\nMy guess is: {guess}")
    attempts += 1
    
    answer = input("Is it higher, lower, or correct? ")

    if answer == "higher":
        low = guess + 1
    elif answer == "lower":
        high = guess - 1
    elif answer == "correct":
        print(f"\nI found secret number in {attempts} tries! and its {secret}")
        break
    else:
        print("Please type 'higher', 'lower', or 'correct'.")