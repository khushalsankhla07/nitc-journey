number = 69
result1 = not (number >= 1 and number <= 100)
print(result1)
result2 = not (number >= 1) or not(number <= 100)
print(result2)
is_employed = False
is_student = False
result3 = not(is_employed or is_student)
result4 = not (is_employed) and not (is_student)
print(result3)
print(result4)