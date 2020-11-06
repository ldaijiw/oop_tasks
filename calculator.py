# calculator

class Calculator:
    def __init__(self):
        
        print("\n\n*****\nCalculator\n*****\n\n")
        self.running = True

        while self.running:
            self.new_calculation()
        
    def new_calculation(self):

        question = input("\nWhat would you like to calculate\n").replace(' ', '')
        if '+' in question:
            num1 = int(question[:question.find('+')])
            num2 = int(question[question.find('+')+1:])
            print(self.add(num1, num2))

        elif '-' in question:
            num1 = int(question[:question.find('-')])
            num2 = int(question[question.find('-')+1:])
            print(self.subtract(num1, num2))
        
        elif '/' in question:
            num1 = int(question[:question.find('/')])
            num2 = int(question[question.find('/')+1:])
            print(self.divide(num1, num2))

        elif '*' in question:
            num1 = int(question[:question.find('*')])
            num2 = int(question[question.find('*')+1:])
            print(self.multiply(num1, num2))
        
        elif 'stop' in question or 'exit' in question:    
            self.running = False
            print("Goodbye")


    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            return "Undefined"
        else:
            return num1 / num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    

if __name__ == "__main__":
    new_calculator = Calculator()