numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
y_ = len(numbers)
numbers.remove(None)# TODO заменить значение пропущенного элемента средним арифметическим
z=sum(numbers)/y_
#n = sum(numbers)/y_
numbers.insert(4, z)
print("Измененный список:", numbers)


#l=[12,78,89,78,32]
#l.remove(78)
#print("вывод:",l)
