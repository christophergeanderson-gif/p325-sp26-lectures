from math import sqrt

a_value = input("Enter a value for a: ")
b_value = input("Enter a value for b: ")
c_value = input("Enter a value for c: ")

a = float(a_value)
b = float(b_value)
c = float(c_value)


solution_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
solution_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(solution_1, solution_2)