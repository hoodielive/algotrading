import time

class Car:
    numberOfWindows = 4
    color = 'iku'
    manufactured = True


def calculate_result(param1, param2):
    result = param1 + param2 * 2
    print('___________________________')
    print('___________________________')
    print(f'Result is: {result}')
    print('___________________________')
    print('___________________________')

for i in range(10):
    sportsCar = Car
    print(f' The sports car has {sportsCar.numberOfWindows} windows.')
    print(f' The sports car\'s color is {sportsCar.color} black.')
    print(f'The iteration number is {i}')
    time.sleep(1)

    a = 0
    while a != 10:
        if (a == 2) or (a == 3) or (a == 4) or (a == 5):
            try:
                print(f'While iteration number {a} and {k}')
                import pdb; pdb.set_trace()
            except Exception as e:
                print('Hey there is an error of sorts.')
                print(e)
                calculate_result(i, a)
        elif a == 4 and i == 3:
            print(f'Hey! a is {a} and i is {i}.')
        else:
            print(f'a is {a}')
            print(f'i is {i}')
            print('Not checked.')
        a += 1
        time.sleep(1)


