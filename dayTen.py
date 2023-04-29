print("Welcome To Calculator App!")

def displayOperation():
    print("+ \n- \n* \n/")

def askOperator():
    operation = input("Enter The Operation: ")
    return operation

firstNumber = int(input("Enter Your First Number: "))
displayOperation()
operator = askOperator()
secondNumber = int(input("Enter Your Second Number: "))

def doTheCalculation(firstNumber, secondNumber, operator):
    if operator == "+":
        return firstNumber + secondNumber
    elif operator == "-":
        return secondNumber - firstNumber
    elif operator == "*":
        return firstNumber * secondNumber
    elif operator == "/":
        if secondNumber == 0:
            return "Invalid Calculation"
        else:
            return firstNumber / secondNumber
    else:
        print("Invalid Calculation")


def showCalculation():
    print("Calculation: " + str(firstNumber) + " " + str(operator) + " " + str(secondNumber) + " = " + str(doTheCalculation(firstNumber, secondNumber, operator)))

showCalculation()


