from math import sqrt

def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant < 0:
       return result  

   if discriminant == 0:
       result.append(-b / (2 * a))
   else:
       result.append((-b + sqrt(discriminant)) / (2 * a))
       result.append((-b - sqrt(discriminant)) / (2 * a))

   return result


def show_result(data):
   if len(data) > 0:
       for index, value in enumerate(data):
           print(f'Корень номер {index+1} равен {value:.02f}')
   else:
       print('Уравнение с заданными параметрами не имеет корней')


def main_first_script():
   a, b, c = map(int, input('Пожалуйста, введите три числа через пробел: ').split())
   result = square_eq_solver(a, b, c)
   show_result(result)
   return result  


def is_palindrome_iterative(s):
  s_lower = s.lower()
  for i in range(len(s_lower) // 2):
    if s_lower[i] != s_lower[len(s_lower) - 1 - i]:
      print("Строка не является палиндромом")
      return False
  print("Строка является палиндромом")
  return True


def main_second_script():
   s = input("Введите строку для проверки на палиндром: ")
   result = is_palindrome_iterative(s)
   return result 


def compute_factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n} равен {factorial}")
    return factorial

def main_third_script():
   s = input("Введите число для расчета факториала: ")
   result = compute_factorial(int(s))
   return result 
	

def main():
    num = input("Введите номер скрипта: 1-квадратное уравление, 2-палиндром, 3-факториал: !!!")
    if int(num) == 1:
      main_first_script()
    elif int(num) == 2:
       main_second_script()
    elif int(num) == 3:
       main_third_script()
    else:
       exit()

if __name__ == '__main__':
   main()
