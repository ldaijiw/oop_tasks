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
            self.num1 = question[:question.find('+')]
            self.num2 = question[question.find('+')+1:]

            self.check_num_is_ans(self.num1, self.num2)
            
            self.ans = self.add(float(self.num1), float(self.num2))

        elif '-' in question:
            self.num1 = question[:question.find('-')]
            self.num2 = question[question.find('-')+1:]

            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.subtract(float(self.num1), float(self.num2))
        
        elif '/' in question:
            self.num1 = question[:question.find('/')]
            self.num2 = question[question.find('/')+1:]

            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.divide(float(self.num1), float(self.num2))

        elif '*' in question:
            self.num1 = question[:question.find('*')]
            self.num2 = question[question.find('*')+1:]
            
            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.multiply(float(self.num1), float(self.num2))
        
        elif 'divisibleby' in question:
            self.num1 = question[:question.find('divisibleby')]
            self.num2 = question[question.find('divisibleby')+11:]
            
            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.divisible_by(float(self.num1), float(self.num2))
        
        elif 'stop' in question or 'exit' in question:    
            self.running = False
            print("Goodbye")
            return
        
        print(self.ans)

    def check_num_is_ans(self, num1, num2):
        try:
            if num1 == 'ans':
                self.num1 = self.ans
            elif num2 == 'ans':
                self.num2 = self.ans
        except AttributeError:
            print("\nNo answer stored in memory, please enter a new calculation\n")
            self.new_calculation()
            return    
            

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