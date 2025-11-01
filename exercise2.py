# bankis balansi

balance = int(input("sheiyvanet tqvens balansze arsebuli tanxa: "))
print("amoirchiet moqmedeba")
print("1 - ganagdeba")
print("2 - tanxis shetana")


choice = int(input("amoirchiet: "))

amount = int(input("raodenoba: "))

if choice == 1:
    if amount > balance:
        print("angarishze sakmarisi tanxa araa")
    else:
        balance -= amount
elif choice == 2:
    balance += amount
else:
    print("shecdoma")

print(f"tqvens angarishze arsebuli balansi sheadgens {balance} lars")

print("-------------")

