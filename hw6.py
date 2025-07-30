# # 1 задание

# arr = [3, 5, 7, 10]

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# target = 7
# print(f"Ищем элемент {target} в массиве {arr}")

# result = linear_search(arr, target)

# if result != -1:
#     print(f"Элемент найден на позиций {result}")
# else:
#     print("Not element")

# # 2 задание
# arr = [1, 3, 5, 7, 9]


# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2 # Находим середину массива
#         center = arr[mid] # Элемент в середине

#         if center == target:
#             print(f"Элемент {target} найден на позиции {mid}")
#             return mid
#         if center > target:
#             print(f"Элемент {target} меньше {center}, ищем в левой половине")
#             right = mid - 1  # Ищем в левой половине
#         else:
#             print(f"Элемент {target} больше {center}, ищем в правой половине")
#             left = mid + 1   # Ищем в правой половине
#     print(f"Элемент {target} не найден в списке")
#     return -1
# binary_search(arr, 5)

# 3 задание

# class SearchEngine:
#     def __init__(self, arr):
#         self.arr = arr

#     def linear_search(self, target):
        
#         for i in range(len(self.arr)):
#             if self.arr[i] == target:
#                 return i
#         return -1 

#     def binary_search(self, target):

#         left, right = 0, len(self.arr) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if self.arr[mid] == target:
#                 return mid
#             elif self.arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1 

# se = SearchEngine([1, 2, 3, 4, 5])
# res1 = se.linear_search(3)
# print(f"Результат линейного поиска: {res1}")
# res2 = se.binary_search(4)
# print(f"Результат бинарного поиска: {res2}")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        
        self.items.append(item)

    def pop(self):
       
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 

    def is_empty(self):

        return len(self.items) == 0

stack = Stack()
print(f"Стек пуст? {stack.is_empty()}") # Ожидаемый вывод: True
stack.push(10)
stack.push(20)
print(f"Элемент извлечен: {stack.pop()}") 
print(f"Стек пуст? {stack.is_empty()}")
print(f"Элемент извлечен: {stack.pop()}") 
print(f"Стек пуст? {stack.is_empty()}")
print(f"Попытка извлечь из пустого стека: {stack.pop()}")
