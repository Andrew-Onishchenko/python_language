#task1--------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	data = []
	for i in range(0, len(elements), 2):
		data.append(elements[i])
return data



def print_data(output_data):
	for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))

#-----------------------------------------


#task2--------------------------
"""
Выведите все четные элементы списка.
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	data = []
	for i in elements:
        if int(i) % 2 == 0:
		data.append(i)
return data



def print_data(output_data):
	for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))


#-----------------------------------------
#task3--------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
def input_data():
	data = input().split() 
	return data

def operation_data(elements):
	data = []
	for i in range(0, len(elements)):
        if i < len(elements)-1:
		if int(elements[i]) < int(elements[i + 1]):
                data.append(elements[i +1])
return data

def print_data(output_data):
	for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))
#-----------------------------------------

#task4--------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, 
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. 
Если таких пар соседей несколько — выведите первую пару.
"""
def input_data():
	data = input().split()
	return data
    
def operation_data(elements):
	data = []
	for i in range(0, len(elements)):
		if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
			data = [elements[i]]
			data.append(elements[i + 1])
                break
return data

def print_data(output_data):
	for i in output_data:
		print (i, end=' ')
print_data(operation_data(input_data()))
#-----------------------------------------

#task5--------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, 
которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
def input_data():
	data = input().split()
	return data
    
def operation_data(elements):
    count=0
    for i in range(1, len(elements)-1):
                if int(elements[i-1])<int(elements[i]) and int(elements[i])>int(elements[i + 1]) :
                    count+=1
return count

def print_data(output_data):
	print (output_data)
print_data(operation_data(input_data()))
#-----------------------------------------


#task6--------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, 
выведите индекс первого из них.
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	data = []max = elements[0]
	data = [max]data.append(0)
	for i in range(1, len(elements)):
        if int(max_elements) < int(elements[i]):
		max = elements[i]data = [max]data.append(i) 
return data
    
def print_data(output_data):
	for i in output_data:
        print (i, end=' ')
        
print_data(operation_data(input_data()))
#-----------------------------------------
#task7--------------------------
"""
Петя перешёл в другую школу. 
На уроке физкультуры ему понадобилось определить своё место в строю. 
Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, 
означающих рост каждого человека в строю. После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.
Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, 
то он должен встать после них.
"""
def input_data():
	data = input().split()
	return data



def operation_data(elements):
	hight = int(input())
	position = 0
	while position < len(elements) and int(elements[position]) >= hight:
		position += 1
		return position

def print_data(output_data):
        print (output_data + 1)
        
print_data(operation_data(input_data()))

#-----------------------------------------
#task8--------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	count=0
	for i in range(0, len(elements)-1):
		if int(elements[i]) != int(elements[i + 1]):
			count+=1
return count

def print_data(output_data):
        print (output_data + 1)


print_data(operation_data(input_data()))

#-----------------------------------------
#task9--------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.
"""
def input_data():
	data = input().split()
	return data
    
def operation_data(elements):
	for i in range(0, len(elements)//2):
		elements[i*2] = elements[i*2 + 1] and elements[i*2 + 1]=elements[i*2]
		return element

def print_data(output_data):
	for i in output_data:
		print (i, end=' ')

print_data(operation_data(input_data()))

#-----------------------------------------
#task10--------------------------
"""
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка.
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	max = elements[0]
	min = elements[0]
	ind_min = 0
	ind_max = 0
	for i in range(0, len(elements)):
		if  int(min) > int(elements[i]):
			min = elements[i]
			ind_min = i
        	if  int(max) < int(elements[i]):
		max = elements[i]
		ind_max = i
		elements[ind_min], elements[ind_max] = elements[ind_max], elements[ind_min]    
return elements

def print_data(output_data):
	for i in output_data:
		print (i, end=' ')

print_data(operation_data(input_data()))


#-----------------------------------------
#task11--------------------------
"""
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k, 
сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. 
Программа сдвигает все элементы, а после этого удаляет последний элемент 
списка при помощи метода pop() без параметров.
Программа должна осуществлять сдвиг непосредственно в списке, 
а не делать это при выводе элементов. Также нельзя использовать дополнительный список. 
Также не следует использовать метод pop(k) с параметром.
"""
def input_data():
	data = input().split()
	return data
    
def operation_data(elements):
	k = int(input())
	for i in range(k, len(elements) - 1):
		elements[i] = elements[i + 1]
		elements.pop()
 return elements
    
def print_data(output_data):
	for i in output_data:
		print (i, end=' ')
        
print_data(operation_data(input_data()))


#-----------------------------------------
#task12--------------------------
"""
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент, 
равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, 
используя метод append.
Вставку необходимо осуществлять уже в считанном списке, не делая этого 
при выводе и не создавая дополнительного списка.
"""
def input_data():
	data = input().split()
	return data

def operation_data(elements):
	data = input().split()
	elements.append(data[1])
	for i in range(len(elements) - 1, int(data[0]), -1):
		elements[i] = elements[i - 1]
		elements[int(data[0])] = int(data[1])
return elements

def print_data(output_data):
	for i in output_data:
		print (i, end=' ')
        
print_data(operation_data(input_data()))


#-----------------------------------------
#task13--------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.
"""
#-----------------------------------------
def input_data():
	data = input().split()
	return data
    
def operation_data(elements):
	count=0
	for i in range(0, len(elements)-1):
		n=i
		n+=1
		for n in range(n, len(elements)):
			if elements[n]==elements[i]:
				count+=1
return count

def print_data(output_data):
        print (output_data)

print_data(operation_data(input_data()))

#task14--------------------------
"""
Дан список. Выведите те его элементы, 
которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, 
в котором они встречаются в списке.
"""
def input_data():
	data = input().split()
return data

    

def operation_data(elements):data=[]
	for i in range(0, len(elements)):
		counter = 0
		for j in range(0, len(elements)):
			if elements[i] == elements[j]:
				counter += 1

        	if counter == 1:
			data.append(elements[i])

return data
  
def print_data(output_data):

    for i in output_data:

        print (i, end=' ')

        
print_data(operation_data(input_data()))            

#-----------------------------------------

#task15--------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. 
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с 
номерами от li до ri включительно. Определите, какие кегли остались 
стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. 
Далее идет K пар чисел li, ri, при этом 1? li? ri? N.
Программа должна вывести последовательность из N символов, где j-й символ 
есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
s = input().split(' ')
outs = ["I" for i in range(int(s[0]))]
for i in range(int(s[1])):
	ns = input().split(' ')
	for f in range(int(ns[0])-1, int(ns[1])):
		outs[f] = "."
for i in outs:
	print(i, end='')

#-----------------------------------------
#task16--------------------------
"""
Условие
Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы они не 
били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
list1 = []
list2 = []
for i in range(8):
	s = input().split(' ')
	s[0] = int(s[0])s[1] = int(s[1])
	list1.append(s[0])
	list2.append(s[1])
if len(list1) == len(set(list1)) and len(list2) == len(set(list2)):
	print('NO')
else:
	print('YES')
#-----------------------------------------