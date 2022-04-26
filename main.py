print("Welcome to Seva's SimpleCalc!")
formula = str(input('Please, enter your equation.\nYou can use numbers and +-*/ operands:\n')).strip()
numbers = '0123456789'
operands = '*/+-'
f_list = []

def is_equation(equ):
    not_equation = 0
    for i in equ:
        if i not in numbers and i not in operands:
            not_equation += 1
    return not_equation == 0


while formula.lower() != "exit":
    result = 'no answer'
#    print(f'your formula is {formula}')
    formula_count = formula.count('*') + formula.count('/') + formula.count('+') + formula.count('-')
    if not is_equation(formula):
        print('ERROR! Not an equation!')
        pass
    if formula[0] not in numbers or formula[-1] not in numbers:
        print('ERROR! Please start and end with a number.')
    if formula_count > 1:
        print('ERROR! Only one operation is permitted. Try again.')
    if formula_count < 1:
        print('ERROR! Please, use +-*/ in the equation.')

    if formula[0] in numbers and formula[-1] in numbers and formula_count == 1 and is_equation(formula):
        if '*' in formula:
            result = int(formula.split('*')[0]) * int(formula.split('*')[1])
        if '/' in formula and int(formula.split('/')[1]) != 0:
            result = int(formula.split('/')[0]) / int(formula.split('/')[1])
        if '/' in formula and int(formula.split('/')[1]) == 0:
            print('ERROR! No division by zero in this calc.')
        if '+' in formula:
            result = int(formula.split('+')[0]) + int(formula.split('+')[1])
        if '-' in formula:
            result = int(formula.split('-')[0]) - int(formula.split('-')[1])
#        for number in formula:
#            f_list.append(number)
#            print(f_list)
        print(f"\nThe answer is: \n{result}\n")
#    else:
#        print("There's an error with your equation, please try again.")
    formula = str(input('Enter another equation, or enter "exit" to finish.\n')).strip()
    f_list = []

print('Thanks for using SimpleCalc!')
