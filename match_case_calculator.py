# Using match case statements for multiple operation in simple calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation + (+, -, *, / ): ")

match operation:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}")
    case "-":
        sub = num1 - num2
        print(f"The result is {sub}")
    case "*":
        multi = num1 * num2
        print(f"The result is {multi}")
    case "/":
        if num2 !=0:
            divs = num1/num2
            print(f"The result is {divs}")
        else:
            print("Cannot be divide by zero")