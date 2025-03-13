class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ArithmeticError("На ноль делить нельзя")
        return a / b

    def pow(self, a, b=2):
        return a ** b

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.divide(s, len(nums))