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
            self.ans = self.add(num1, num2)

        elif '-' in question:
            num1 = int(question[:question.find('-')])
            num2 = int(question[question.find('-')+1:])
            self.ans = self.subtract(num1, num2)
        
        elif '/' in question:
            num1 = int(question[:question.find('/')])
            num2 = int(question[question.find('/')+1:])
            self.ans = self.divide(num1, num2)

        elif '*' in question:
            num1 = int(question[:question.find('*')])
            num2 = int(question[question.find('*')+1:])
            self.ans = self.multiply(num1, num2)
        
        elif 'divisibleby' in question:
            num1 = int(question[:question.find('divisibleby')])
            num2 = int(question[question.find('divisibleby')+11:])
            self.ans = self.divisible_by(num1, num2)
        
        elif 'stop' in question or 'exit' in question:    
            self.running = False
            print("Goodbye")
        
        print(self.ans)


    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            return "Undefined"
        return num1 / num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        return False
    
    

if __name__ == "__main__":
    new_calculator = Calculator()