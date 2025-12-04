class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(result)
        return result

    def previous_result(self):
        if self.history:
            return self.history[-1]
        return None

    def multiply(self, a, b):
        result = a * b
        self.history.append(result)
        return result