# calculator
import math

class Calculator:
    def __init__(self):
        
        print("\n\n*****\nCalculator\n*****")
        print("""
        Options:
        Addition: +
        Subtraction: -
        Division: /
        Multiplication: *
        Check if a number is divisible by another (returns True/False): divisible by
        Work out the area of a shape: area
        Inch/cm converter: inches or cm
        
        Answer is also stored in memory and can be used for future calculations: ans
        """)
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
        
        elif 'cm' in question:
            self.num1 = question[:question.find('cm')]
            self.ans = self.inch_cm_convert(float(self.num1), 'cm')
        
        elif 'inch' in question:
            self.num1 = question[:question.find('inch')]
            self.ans = self.inch_cm_convert(float(self.num1), 'inch')
        
        elif 'area' in question:
            area_question = input("\nWhat shape would you like to calculate the area for?\n(Triangle/Circle)\n")

            if 'triangle' in area_question:
                base = input("\nBase length?\n")
                height = input("\nHeight length?\n")
                self.ans = self.triangle_area(float(base), float(height))
            
            elif 'circle' in area_question:
                radius = input("\nRadius length?\n")
                self.ans = self.circle_area(float(radius))
        
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
    
    
    def inch_cm_convert(self, num1, convert_from):
        if convert_from == "inch":
            return num1 * 2.54
    
        elif convert_from == "cm":
            return num1 / 2.54

    
    def triangle_area(self, base, height):
        return base * height / 2

    def circle_area(self, radius):
        return math.pi * (radius**2)


if __name__ == "__main__":
    new_calculator = Calculator()