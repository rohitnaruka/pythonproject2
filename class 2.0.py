
#1.write a python script to merge two python dict

# dict1={'rohit':19,"rahul":20}
# dict2={'ritu':18,"ram":12}
# def merge_two_dict(dict1,dict2):
#     merged_dict=dict1.copy()
#     for key ,value in dict2.items():
#         merged_dict[key]=value
#     return merged_dict
# print(merge_two_dict(dict1,dict2))


#2.write a python program to sum all the items in a dict

# my_dict={ 1:10,3:21,4:32,7:20}
# def sum(my_dict):
#     total=0
#     sum=0
#     for key,value in my_dict.items():
#         sum += key
#         total += value
#     return total,sum
# print(sum(my_dict))

#
#value
# my_dict={'rohit':19,"rahul":20}
# def sum_all_items(my_dict):
#     total_sum=0
#     for value in my_dict.values():
#         total_sum+=value
#     return total_sum
# print(sum_all_items(my_dict))
#
# #3.write a python program to multiply all the items in a dict
#
# my_dict={ 1:10,3:21,4:32,7:20}
# def sum(my_dict):
#     x=1
#     y=1
#     for key,value in my_dict.items():
#         x *= key
#         y *= value
#     return y,x
# print(sum(my_dict))
#
# #4.wirte a python program to remove a key from a dict
# import random
#
# my_dict={'rohit': 19, 'rahul': 20, 'ritu': 18, 'ram': 12}
# def remove_key(my_dict):
#     new_dict={}
#     for key ,value in my_dict.items():
#         if key !=key_to_remove:
#             new_dict[key]=value
#     return new_dict
# key_to_remove='rahul'
# print(remove_key(my_dict))
#
# #5.write a python program to sort a given dict by key
# my_dict={'rohit': 19, 'rahul': 20, 'ritu': 18, 'ram': 12}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for keys,value in sorted(my_dict.items()):
#         new_sorted_dict[value]=keys
#     return new_sorted_dict
# print(sorted_dict(sorted_dict(my_dict)))
#
# #values
# my_dict={'rohit': 19, 'rahul': 20, 'ritu': 18, 'ram': 12}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for i in sorted(my_dict.keys()):
#         new_sorted_dict[i]=my_dict[i]
#     return new_sorted_dict
# print(sorted_dict(my_dict))
#
#6.Write a Python program to get the maximum and minimum values of a dictionary.
#
# my_dict={'x':500,'y':5874,'z':560}
# def max_min(my_dict):
#     max_key=None
#     max_value=float('-inf')
#     min_value=None
#     min_key=float('inf')
#     for key,value in my_dict.items():
#         if value>max_value:
#             max_key=key
#             max_value=value
#         if value<min_value:
#             min_key=key
#             min_value=value
#     return max_key,max_value,min_key,min_value
# print(max_min(my_dict))

#7.remove duplictein _nested_dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# #duplicate kite baar aaya h
# def remove_duplicate(student_data):
#     new_dict={}
#     for key,value in student_data.items():
#         if value not in new_dict.values():
#             new_dict[key]=value
#     return new_dict
# print(remove_duplicate(student_data))

# #8.write a python program to select an item randomly from a list.
#
# import random
# list=[1,5,4,2,36,5,8,7]
# def a(list):
#     ran=random.choice(list)
#     return ran
# print(a(list))
# #
# #
# #9.find the second_smallest_num
# list=[1,2,3,4,5,6,7]
# def find_2nd_smallest(list):
#     sorted_list=sorted(list)
#     second_smallest=sorted_list[1]
#     return second_smallest
# print(find_2nd_smallest(list))
# #
# #10.reverese a list
# list=[1,4,7,9,0,8,7,7,9]
# def reverse_list(list):
#     reversed_list = []
#     for i in reversed(list):
#         reversed_list.append(i)
#     return reversed_list
# print(reverse_list(list))
# #
# #
# #11.write a python script to add a key  to a dict
# my_dict={'a':'rohit','age':90}
# my_dict['city']='jaipur'
# print(my_dict)
# #
# #Write a Python script to concatenate the following dictionaries to create a new one
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# def concatenate_dicts(*dicts):
#     new_dict={}
#     for d in dicts:
#         new_dict.update(d)
#     return new_dict
# concatenate_dicts=concatenate_dicts(dic1,dic2,dic3)
# print(concatenate_dicts())
#
# #
# import random
# list=[1,5,4,2,36,5,8,7]
# def a(list):
#     ran=random.choice(list)
#     return ran
# print(a(list))

# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# def remove_count_duplicate(student_data):
#     value_count={}
#     duplicate_count=0
#     deduplicated_dict={}
#     for key,value in student_data.items():
#         if value in value_count:
#             value_count[value]+=1
#             if value_count[value]==2:
#                 duplicate_count +=1
#         else:
#             value_count[value]=1
#             deduplicated_dict[key]=value
#     return duplicate_count,deduplicated_dict
# print(remove_count_duplicate(student_data))


# def count_and_remove_duplicates(input_dict):
#







#new
#Example usage:
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#
#    },
# }
# def count_name(student_data):
#     #duplicate_count=0
#     count=0
#     for key,value in student_data.items():
#        count=count+1
#     return count
# print(count_name(student_data))


# def count_duplicate(student_data):
#     duplicate_count=0
#     name_count={}
#     for id,data in student_data.items():
#         name=data['name'][0]
#         if name in name_count:
#             name_count[name]+=1
#             if name_count[name]==2:
#                 duplicate_count+=1
#         else:
#             name_count[name]=1
#     return duplicate_count
# duplicate=count_duplicate(student_data)
# print(count_duplicate(student_data))



# Example usage:
student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
    'id5':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },

 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}
#def duplicate_name(student_data):
duplicate={}
result={}
for key ,value in student_data.items():
    if value not in result.values():
        result[key]=value
    else:
        duplicate[key]=value
    #return result,duplicate
print(result,'\n',duplicate)




# add items in multiple dict .
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#     'id5':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  }
# def add_address_of_student(student_data):
#     for student_id in student_data:
#         student_data[student_id]['adress']=[{
#             'id1':'jaipur',
#             'id2':'jodhpr',
#             'id3':'kota',
#             'id4':'tonk'
#         }]
#         add_address_of_student(student_data)
# print(add_address_of_student(student_data))

# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# def add_key_value(student_data):
#     new_key_value={'adress':2}
#     for i in student_data:
#         student_data[i]['adress']='jaipur'
#     return student_data
# print(add_key_value(student_data))


# new_list = [id1,id2,id3,id4]
# for i in new_lsit:
#      if i in student_data:
#          studentdata[i][key]= value
#      else:
#          student_datta[i]={key:vaue}
# print(student_data)

# remove duplicate ,
# remove duplicate count,
# remove duplicate name print