#1 Write a Python program to generate and print a list, where the values are square of numbers between 1 and 30 (both included)
def printValues():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print(l)
printValues()

print('----------------')

#2 Write a Python program to display the examination schedule.
exam_st_date = (11, 12, 2014)
print('The examination will start from : %i / %i / %i' %exam_st_date)

print('----------------')

#3 Write a Python program which accepts a sequence of commaseparated numbers from user and generate a list and a tuple with those numbers.
x = input('Input a sequence of commaseparated numbers: ')
list = x.split(',')
tuple = tuple(list)
print('List :' , list)
print('Tuple :' , tuple)

print('----------------')

#4 Write a Python function that takes two lists and returns True if they have at least one common member.
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

#5 Write a Python-script.
bus_array = [(10,0), (3,5), (5,8)]
passengers_left = sum([entered - left for entered, left in bus_array])
print('Passengers left : ', passengers_left)




