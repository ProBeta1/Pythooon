#Basic calculator in python
print('-------------------------------')
print('Enter first number : ')
num1 = int(input())
print('Now choose the operation (+ - * / **) : ')
op = input()
print('Enter the second number : ')
num2 = int(input())
if op=='+':
        print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op=='/':
    if num2==0:
        print('WARNING.....Divide By Zero Error....')
    else:
        print(num1/num2)
elif op=='**':
    print(num1 ** num2)
print('THANK YOU!!!!!')
