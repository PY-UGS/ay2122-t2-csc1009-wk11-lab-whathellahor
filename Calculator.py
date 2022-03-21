class Calculator:

    # Constructor
    def __init__(self, input1, input2):
        self.input1 = float(input1)
        self.input2 = float(input2)

    # Perform addition operation
    def adder(self):
        return self.input1 + self.input2

    # Perform subtraction operation
    def subtractor(self):
        return self.input1 - self.input2

    # Perform multiplication operation
    def multiplier(self):
        return self.input1 * self.input2

    # Perform division operation
    def divider(self):
        return self.input1/self.input2

    # Clear both values
    def clear(self):
        self.input1 = self.input2 = 0


num1 = input("Enter your first number: ")   # Takes in first input from user
num2 = input("Enter your second number: ")  # Takes in second input from user
calculator = Calculator(num1, num2)         # Pass both inputs into class

print("Addition: ", calculator.adder())             # Prints the results of addition operation
print("Subtraction: ", calculator.subtractor())     # Prints the results of subtraction operation
print("Multiplication: ", calculator.multiplier())  # Prints the results of multiplication operation
print("Division: ", calculator.divider())           # Prints the results of division operation
print("Clear: ", calculator.clear())                # Prints the results of the values after clearing