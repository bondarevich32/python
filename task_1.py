#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

try:
    arg1 = int(input("Введите Делитель "))
    arg2 = int(input("Введите Делитель "))
    res = arg1 / arg2
except ValueError:
    return 'Ошибка значения'
except ZeroDivisionError:
    return "На ноль делить нельзя!"

return res

if arg2 != 0:
    return arg1 / arg2
else:
    print("Значение не может быть равно нулю")

print(f'result  {div()}')