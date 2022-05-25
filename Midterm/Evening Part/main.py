from bmicalculator import BMICalculator
from bmicalculatorUI import BMICalculatorUI

if __name__ == '__main__':
    calculator = BMICalculator()
    ui = BMICalculatorUI(calculator)
    ui.mainloop()
