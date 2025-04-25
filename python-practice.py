lst =  [2,4,6,8,10,12,14, 3, 7, 9, 1, 21]

sum = 0
for i in lst:
      sum += i

print(f"Sum of elements in the list: {sum}")

#For odd numbers
lst_odd = []

for i in lst:
    if i % 2 != 0:
       lst_odd.append(i)

print(f"Odd elements in the list: {lst_odd}")

#For Computing Factorial
def Factorial(a):
    try:
        a = int(a)
    except ValueError:
          return "invalid input!"
    if a < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, a+1):
        result *= i
    return result
print(f"The factorial is : {Factorial(5)}")

#For string recursion

def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

my_string = " my name is cedrick "
reversed_string = reverse_string_recursive(my_string)
print(f"Original string: '{my_string}'")
print(f"Reversed string: '{reversed_string}'")

# for factorial recursive

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

numbers_to_calculate = [2, 4, 6, 8, 10, 12, 14, 3, 7, 9, 1, 21]

factorials = {}

for num in numbers_to_calculate:
    result = factorial_recursive(num)
    factorials[num] = result
    print(f"The factorial of {num} is: {result}")

print("\n--- All Factorial Results ---")
for number, fact in factorials.items():
    print(f"Factorial of {number}: {fact}")

#For Sum of digits

def sum_digits(n):
  s = 0
  while n:
    s += n % 10
    n //= 10
  return s

number = 5640330
result = sum_digits(number)
print(result)