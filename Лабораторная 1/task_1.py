numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None)
sum_without_missing = sum(num for num in numbers if num is not None)
total = len(numbers)
average = sum_without_missing / total
numbers[missing_index] = average
print("Измененный список:",numbers)
