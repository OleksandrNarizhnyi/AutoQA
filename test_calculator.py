from calculator import Calculator

calculator = Calculator()

# test method sum
res = calculator.add(4, 6)
assert res == 10, 'результат не совпал'

res = calculator.avg([1, 2, 3, 4, 5])
assert res == 3, 'результат не совпал'