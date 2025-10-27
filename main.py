#Prompt User to input amount of coffee grounds
Coffee_str = input("Enter Amount of coffee grounds in grams: ")
Coffee_int = int(Coffee_str)
x = int(Coffee_str)

#Prompts User for Coffee to Water Ratio Preference and provides output
print("Enter desired coffee to water ratio: 1/16 or 1/17")
y = input()

if y == "1/16":

    print(x * 16,"grams of water")

else:

    print(x * 17,"grams of water")

