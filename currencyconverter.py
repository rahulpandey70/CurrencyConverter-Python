with open ('currency.txt') as f:
    lines = f.readlines()


currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    #print(parsed)

Amount = int(input("Enter Amount: "))
print("\n\t Enter the name of currency you want to convert this amount to? Available options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("\n\t Please enter one of these values: \n")
print(f"{Amount} INR is equal to :\n\t{Amount *float(currencyDict[currency])} {currency}\n")

    