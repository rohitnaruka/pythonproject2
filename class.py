#.write a program and find out the avrage_value.

# my_list=[10,10,10]
# def find_avrage(my_list):
#     sum = 0
#     for i in my_list:
#         sum=i+sum
#         0=10+0=10=10+10=20=10+20=30
#         sum+=i
#         #0+=10,10+=10,20+=10,30
#         avrage =sum / len(my_list)
#     return avrage
# print(find_avrage(my_list))


#2 multiplie the numbers
# my_list = [1,2,8,5,8]
# def multiplie_num(my_list):
#     x = 1
#     for i in my_list:
#          x=i*x
#          #1=1*1,1=2*1,2=8*2,16=5*16,80=8*80,=640
#          #x*=i
#         #1*=1,1*=2,2*=8,16*=5,80*=8,=640
#     return x
# print(multiplie_num(my_list))

#3convert the two list in one dict.
# list1 = ["r","n","p","x"]
# list2 = [10,20,30,40]
# def lists_to_dict(keys,values):
#     result_dict={}
#     for i in range(len(keys)):
#         if len(keys) !=len(values):
#             result_dict[keys[i]]=values[i]
#     return result_dict
# print(lists_to_dict(keys=["r","n","p","x"],values=[10,20,30,40]))

#
# # 4 write a  Python program to print positive numbers in a list.
# my_list=[1,2,5,6,8,7,4,10,30,50]
# def find_positive_numbers(my_list):
#     positive_num =[]
#     for i in my_list:
#         if i > 0:
#             positive_num.append(i)
#     return positive_num
# print(find_positive_numbers(my_list))
#
# #5.write a  Python program to print negetive numbers in a list.
# my_list=[10,-2,34,3,-3,4,-5,6,8,-1]
# def negitive_numbers(my_list):
#     sum=0
#     negitive_numbers=[]
#     for i in my_list:
#         if i <0:
#             sum+=i
#             negitive_numbers.append(i)
#     return negitive_numbers,sum
# print(negitive_numbers(my_list))
# #
# # 6.write a python program to count all positive number ,\
# my_list = [1,-2,-3,3,4,-5,6,-5,-4,-6,5,9,4,9]
# def count_positive_num(my_list):
#     count = 0
#     positive_num=[]
#     for i in my_list:
#         if i>0:
#           count+=i
#           positive_num.append(i)
#     return positive_num,count
# print(count_positive_num(my_list))
#
# #7.write a python program find average value of a dictionary.
# names = {"ritu": 20, "ridhi": 30, "nidhi": 40}
# def average_value(my_list):
#     sum = 0
#     average=[]
#     for i in my_list:
#         sum+=i
#         average=sum/len(my_list)
#     return average
# print(average_value(my_list))
#
# #8.write a pyton program a find even number in a given dictionary and output show be in list.
# nums = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
# def find_even_numbers(nums):
#     even_numbers=[]
#     for i in nums.values():
#         if i % 2==0:
#             even_numbers.append(i)
#     return even_numbers
# print(find_even_numbers(nums))
#
# #9.write a pyton program a find odd number in a given dictionary and output will be show in a list.
# nums = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
# def find_odd_numbers(nums):
#     odd_numbers=[]
#     for i in nums.values():
#         if i % 2!=0:
#             odd_numbers.append(i)
#     return odd_numbers
# print(find_odd_numbers(nums))
#
#
# #10.wite a python program and find max number in a given dictionary.
# def find_max_in_dict(input_dict):
#     max_value=None
#     for value in input_dict.values():
#         if max_value is None or value > max_value:
#             max_value=value
#     return max_value
# my_dict = {'x':1,'y':2,'z':3,'a':4,'b':5,'c':6}
# result = find_max_in_dict(my_dict)
# print(result)
#
#
# #11.wite a python program and find min number in a given dictionary.
# def find_min_in_dict(input_dict):
#     min_value=None
#     for value in input_dict.values():
#         if min_value is None or value < min_value:
#             min_value=value
#     return min_value
# my_dict = {'x':1,'y':2,'z':3,'a':4,'b':5,'c':6}
# result = find_min_in_dict(my_dict)
# print(result)
#
#
# # 12.write a program and marge two python dictionary into one.
# dict1 = {"r": 12, 'k' : 13,"n": 10}
# dict2 = {"x": 1, "y": 2, "z": 3}
# def merge_two_dict(dict1,dict2):
#     merged_dict=dict1
#     for key,value in dict2.items():
#         merged_dict[key]=value
#     return merged_dict
# print(merge_two_dict(dict1,dict2))
#
# #13.write a python program and find sum_of_dictionary_values.v
# dict = {"r":1,"k":2,"n":3,"s":9,"g":6}
# def sum_of_dictionary(dict):
#     sum=0
#     for values in dict.values():
#         sum+=values
#     return sum
# print(sum_of_dictionary(dict))
#
# # 14.write a python program and find sum of key and value in pyhton dictionary
#

# #15. write a Python program and find the maximum value and its key in the dictionary and convert it into 
# #  list.(output will be show in list of dictionary)
dict = {
"ridhi":21,
"nidhi":12,
"raj": 19,
"dipti":51,
"swetae":13
 }
def find_maximum_value_key(dict):
    max_key = None
    max_value=None
    for key,value in dict.items():
        if max_value is None or value>max_value:
            max_key=key
            max_value=value
    return max_key,max_value
print(find_maximum_value_key(dict))


#
# #LIST-:
# # 1.print all positive numbers in a range:
# list=[5,7]
# def find_positive_numbers(list):
#     positive_numbers=[]
#     for i in range(5,7):
#         if i > 0:
#             # print(i)
#             positive_numbers.append(i)
#     return positive_numbers
# print(find_positive_numbers(list))
#
#
# #2.print all positive numbers in a range:
# def find_nagitive_numbers(start,end):
#     nagitive_numbers=[]
#     for i in range(start,end+1):
#         if i < 0:
#             # print(i)
#             nagitive_numbers.append(i)
#     return nagitive_numbers
# start_range=-17
# end_range=-98
# print(find_nagitive_numbers(start_range,end_range))
#
#
# #3.reverse all list.
list=[1,4,7,9,0,8,7,7,9]
def reverse_list(list):
    reversed_list = []
    for i in reversed(list):
        reversed_list.append(i)
    return reversed_list
print(reverse_list(list))
#
#
# # 4.find comman items from two list.
# list1=['white','black','red','green','yellow']
# list2=['sky','blue','white','red','dark']
# def find_comman_items(list1,list2):
#     comman_items = []
#     for item1 in list1:
#         for item2 in list2:
#             if item1 == item2:
#                 comman_items.append(item1)
#     return comman_items
# print(find_comman_items(list1,list2 ))
# None=the none is used to define a null variable or an object
#is =is used to test if two variables refer to the same object

# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
#     "hiyu":{"age":7, "address":"bikaner"}
# }
# def find_max_number(student):
#     max_number =
#     for value in student.items():
#             if max_number is
#                 max_number=value
#     return max_number
# print(find_max_number(student))


# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
#     "hiyu":{"age":7, "address":"bikaner"}
# }
# def find_max_number(student):
#     max_number = None
#     for i in student.keys():
#         if max_number is None or student[i]['age'] > max_number:
#             max_number = student[i]['age']
#     return max_number
# print(find_max_number(student))



# def swaplist(newlist):
#     size = len(newlist)
#     temp = newlist[0]
#     newlist[0] = newlist[size - 1]
#     newlist[size - 1] = temp
#     return newlist
# newlist =[12,35,9,56,24]
# print(swaplist(newlist))
#
# list = []
# num =int(input("how many elements in list?:"))
# for x in range(num):
#     numbers = int(input('enter numbers'))
#     list.append(numbers)
# print("\nmaximum element in the list is :",max(list))
# print("minimum element in the list is:",min(list))
#
# list = [1,'ABC',2,3,'abc','XYZ',4]
# print("The first half of the list",list[:3])
# print("The second half of the list",list[3:])
#
# list1 = [1,'ABC',2,3,'abc','XYZ',4]
# length_to_split = [len(list1)//2]*2
# print(length_to_split)
# iterable_lst = iter(list1)
# res_list = [list((iterable_lst,elem)) for elem in length_to_split]
# print("initial list:",list1)
# print("List halves after splitting",res_list)
#
# list =['' ,'27','37','','45','24']
# print('original list:',str(list))
# while("" in list):
#     list.remove("")
#     print("list after removing empty strings:",str(list))
#
# list = ["",'ROHIT','SINGH','','NARUKA','RAJPUT']
# print("original list:",str(list))
# list = [x for x in list if x]
# print("list after removing empty strings:",str(list))
#
# list1 =['XYZ','ABC','xyz','abc']
# list1[0],list1[-1] = list1[-1],list1[0]
# print("list after swapping:",str(list1)
#
# def iterate(d):
#     for key, values in d.items():
#
#         print(key,values)
#
# print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3}))
#
# copy:-
# def iterate(x):
#     for key,values in x.items():
#         print(key,values)
# print(iterate(x={'rohit':18, 'ritu':17, 'kuldeep':20}))
#
#
# def add(D):
# D = {1 : 4, 2 : 3,  5 : 6 }
# sum = 0
# total = 0
# for key ,values in D.items():
#     total+=values
#     sum+=key
# print(sum,total)
#
# copy
# x = {234 : 235, 123 : 132,231 : 312}
# sum = 0
# total =0
# for key,values in x.items():
#     total+=key
#     sum+=values
# print(sum,total)
#
# def remove(dict):
#     if 'a' in dict:
#         del dict['a']
#     return dict
#
# print(remove(dict = {1 : 4, 'a' : 3,  5 : 6 }))
#
# copy:-
# def remove(dict):
#     if  'b' in dict:
#         del dict['b']
#     return dict
# print(remove(dict={'b': 1 , 2:3 , 5:6 }))
#
#
# def merge_two(dict_1,dict_2):
#     x = dict_1.copy()
#     x.update(dict_2)
#     return x
# print(merge_two(dict_1=({'a': 10, 'b': 8}),dict_2 = {'d': 6, 'c': 4}))
#
# copy:-
# def add_two(dict_1,dict_2):
#     x=dict_1.copy()
#     x.update(dict_2)
#     return x
# print(add_two(dict_1=({'a':25, 'b':25}),dict_2={'d':25,'c':25}))
#
# m

# D1 = {'emp1': {'name': 'Jim', 'age': 26, 'job': 'developer'},
#       'emp2': {'name': 'Sam', 'age': 30, 'job': 'data analyst'},
#       'emp3': {'name': 'Dean', 'age': 29, 'job': 'data scientist'},
#       'emp4': {'name': 'Leo', 'age': 25, 'job': 'python developer'}}
#
# # Actual dictionary
# print("The actual dictionary is:", D1)
# # Change the value of a dictionary
# D1['emp3']['age'] = 24
# # Updated dictionary
# print("The updated dictionary is:", D1)
#
# keys = ['first_name', 'age', 'job', 'company']
# values = ['Jim', 23, 'developer', 'XYZ']
#
# # map using zip()
# D1 = dict(zip(keys, values))
# print(D1)
#
#
# D1 = {9,5,8,80,8,0,9,8,8}
#
# print("The actual dictionary is:", str(D1))
#
# # checking if empty or not
# result = not bool(D1)
# print("Is the given dictionary empty? :", result)
#
#
#
# D1 = {'Jim': 23, 'Sam': 29, 'Dean': 33, 'Micheal': 40}
#
# # Python code to find key with Maximum value in Dictionary
# Key_max = max(D1, key=lambda x: D1[x])
# Key_min = min(D1, key=lambda x: D1[x])
# print("The key with maximum value:", Key_max, ",& corresponding value:", D1[Key_max])
# print("The key with minimum value:", Key_min, ",& corresponding value:", D1[Key_min])
#
#
# D1 = {'Jim': 23, 'Sam Winchester': 29, 'Dean Winchester': 33, 'Micheal': 40}
#
# # search substring
# search_string = "Winchester"
# # Actual dictionary
# print("The actual dictionary is:", str(D1))
#
# res_string = dict(filter(lambda item: search_string in item[0], D1.items()))
#
# # Resultant dictionary
# print("The Key-Value pair for search keys ::", str(res_string))
#
#
# D1= {'Jim': 23, 'Sam Winchester': 29, 'Dean Winchester': 45, 'Micheal': 40}
#
# #
# def getKey(dict_val):
#     for dict_key, value in D1.items():
#         if dict_val == value:
#             return dict_key
#     return "key doesn't exist"
#
#
# print("Get key of value 40:", getKey(40))
# print("Get key of value 20:", getKey(45))
#
# D1 = {'Jim': 23, 'Jerry': 29, 'Micheal': 40, 'Merlin': 45, 'Antony': 34}
#
# D1 = sorted(D1.items())
# print(D1)
#
# x1={"rohit": 18, "ritu": 17, "bitu":21}
# keys = ("kuldeep":19,)
#
# list =["banana","apple","mango","cherry"]
# first_item =list[0]
# print(first_item)
#
# list =[]
#
#
# list = [1,2,34,56,7]
# print(len(list))
#
# list = [24,53,83,46,90]
# print(str(list))
#
#
# list =[23,45,67,8,9]
# list[4]=23
# list[0]=9
# print(list)
#
# list =[13,24,35,67]
# list[0]=35
# list[2]=13
# print(list)
#
# list =[1,2,3]
# def get_maxium(list):
#    max = 0
#    for i in list:
#       if i > max:
#          max = i
#    return max
# print(get_maxium([1,2,3,5]))
#
# def get_minium(list):
#    min = 7
#    for i in list:
#       if i < min:
#          min = i
#    return min
# print(get_minium([1,2,3,4,5,6,7]))