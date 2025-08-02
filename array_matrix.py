class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)

    def access(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None


class Matrix:
    def __init__(self, rows, cols, default=0):
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def access(self, row, col):
        return self.data[row][col]

    def delete(self, row, col):
        self.data[row][col] = 0  # or some default/None
