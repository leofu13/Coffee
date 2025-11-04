#Input Validation
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please input a numerical value.")
            continue
        else:
            return userInput
            break
#Prompt user to input the amount of coffee grounds
Coffee_str = inputNumber("Please input amount of coffee grounds in grams: ")
x = Coffee_str

#Prompts User for Coffee to Water Ratio Preference and provides output
Brew_ratio = input("Enter desired coffee to water ratio: 1:16 or 1:17: ")
y = Brew_ratio

if y == "1:16":

    print(x * 16,"grams of water")

else:

    print(x * 17,"grams of water")

