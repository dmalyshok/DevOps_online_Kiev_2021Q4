# Реализовать скрипт, который решает квадратное уравнение вида 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0.
# Параметры квадратного уравнения 𝑎, 𝑏, 𝑐 задаются вводом или через аргументы командной строки.
# В скрипте реализовать несколько функций, которые декомпозируют задачу решения квадратного
# уравнения. В эти функции должны передаваться параметры. Также на эти функций написать UnitTests.
# Основной скрипт solv_square_equation.py должен иметь следующие функции:
# - main()
# - validate_param(int) - проверяет, что введено число, повторяет ввод 3 раза если не число
# (использовать exception)
# - discriminant(a, b, c)
# - roots(d, a, b, c)
# - solv_square(a, b, c) -> roots
# - square_print(a, b, c, roots) – выводит на экран результат
# на выделенные написать UnitTest.
# Не использовать глобальные переменные.

def validate_param(int):
    i = 0
    while True:
        try:
            int = int(input())       
        except ValueError:
            print("Not an integer! Try again.")
            if i == 2:
                break
            else:
                i += 1
                continue
        else:
            return int 
            break 

def discriminant(a, b, c):
    d = (b ** 2) - (4 * a * c)
    roots (d, a, b, c)
    return d

def roots(d, a, b, c):
    # если D < 0, корней нет;
    # если D = 0, есть один корень;
    # если D > 0, есть два различных корня.
    #print('i am from roots ' + str(a) + str(b) + str(c) + str(d) )
    if d < 0:
        print('Quadratic equation have not roots')
        return 'd < 0'
    elif d == 0:
        #х = −b/2a
        root = -b/(2*a)
        print('Quadratic equation have 1 roots '+ str(root) + ' from quadratic equation '+ str(a) + 'x**2' + '+' + '('  + str(b) + ')' + 'x' + '+' + '(' + str(c) + ')' '=0')
        return 'd == 0'
    elif d > 0:
        print('Quadratic equation have two roots')
        solv_square(a, b, c)
        return 'd > 0'
        

def solv_square(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b + (d**0.5))/(2*a)
    root2 = (-b - (d**0.5))/(2*a)
    roots = str(root1) +' and '+ str(root2)
    square_print(a, b, c, roots)
    return root1,root2

def square_print(a, b, c, roots):
    print('Roots are: ' + str(roots) + ' from quadratic equation '+ str(a) + 'x**2' + '+' + '('  + str(b) + ')' + 'x' + '+' + '(' + str(c) + ')' '=0' )
    #return None

def main():
    print('Enter fist member A: ')
    a = validate_param(int)
    #print(a)
    if a == 0:
        print('Bad way for quadratic equation a=0')
        exit
    elif a != None:
        print('Enter fist member B: ')
        b = validate_param(int)
        #print(b) 
        print('Enter fist member C: ')
        c = validate_param(int)
        #print(c) 
        discriminant(a, b, c)
    else:
        exit

if __name__ == "__main__":
    main()

