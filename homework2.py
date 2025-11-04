print("---------------------")

name = "Tornike"

age = 25

have_coded_before = True

print("Name", name)
print("age", age)

if have_coded_before:
    print("yes,i have coded before")
    
else:
    print("no i didnot")

favorite_language_program = input(("which program language is your favorite?: "))

print(f"favorite language program: {favorite_language_program}")

# tu cifris chawera stringshic sheidzleba rogor mivutitot is rom am kitxvashi ricxvebis gamoyeneba arsheidzleba


print("---------------------")

num1 = str(input("Enter number: "))

num2 = str(input("Enter second number: "))

print(type(num1))
print(type(num2))


print("compare numbers", num1 > num2)

num1 = int(num1)
num2 = int(num2)

print("compare numbers and choose action: > , < or =")

# rogor gavagrdzelebinot erroris shemtxvevashi dzveli kitxva da axalze ar gadavides. 

choice = input()

if choice == ">":
    print(num1 > num2)
elif choice == "<":
    print(num1 < num2)
elif choice == "=":
    print(num1 == num2)
else:
    print("Error choose > , < or = ")

print("---------------------")

minutes = int(input("enter minutes: "))


hours = minutes // 60

remaining_minutes = minutes % 60



print(f"your entered minutes is {hours} hour and {remaining_minutes} minutes")


print("---------------------")




energy_level = (int(input("choose your energy level with a 1-5 scale: ")))

if energy_level < 3:
    print("please take a long rest before return :)")
elif energy_level == 3:
    print("take a short break")
elif energy_level > 3:
    print("you're good continue studying")
else:
    print("error choose energy level between 1 and 5 ")


print("packed study shcedule" if minutes > 180 and energy_level <= 4 else "youre good but you can more")

# energy level wesit naklebi unda iyos ro davuwerot gadatvirtuli grafiki . mgoni :D 

# bolo printis else armindoda carieli dametovebina mgoni arjdeba logikurad :D 