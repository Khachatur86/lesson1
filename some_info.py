user_info = {'first_name':'Khachatur', 'last_name':'Sarkisyan'}

print(user_info.get('first_name'))

numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append('Python')
print(len(numbers))
numbers.remove('Python')
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2:5])

# class CustomDictionary(dict):
#
#     def __getattr__(self, item):
#         return self[item]
#
# d = CustomDictionary({'a':5})

# d.update({'p':3, 'b':4})
# # print(d)

# print(d.5)


class CustomClass(list):
    def __init__(self, list):
        super().__init__(list)
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self[self.n]
        self.n += 1
        if self.n == len(self) - 1:
            self.n = 0
        return result


f = CustomClass([1, 2, 3, 4, 5])

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


class MyContextManager:
    def __init__(self, f_name):
        self.f_name = f_name

    def __enter__(self):
        self.file = open(self.f_name)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        del self.file
