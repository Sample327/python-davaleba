# yvelaze didi ricxvi,dabali da sashualo

num1 = int(input("sheiyvanet pirveli ricxvi: "))
num2 = int(input("sheiyvanet meore ricxvir:"))
num3 = int(input("sheiyvanet mesame ricxvi:"))
print("-------------")

print("amoirchiet moqmedeba")
print("1 - yvelaze magali ricxvi")
print("2 - yvelaze dabali ricxvi")
print("3 - aritmetikuli sashualo")

choice = int(input("amoirchiet: "))

average = (num1 + num2 + num3) / 3

if choice == 1:
    print(f"yvelaze magali ricxvia {max(num1,num2,num3)}")

elif choice == 2:
    print(f"yvelaze dabali ricxvia {min(num1,num2,num3)}")
elif choice == 3:
    print(f"ricxvebis sashualo aris {average}")

print("-------------")
