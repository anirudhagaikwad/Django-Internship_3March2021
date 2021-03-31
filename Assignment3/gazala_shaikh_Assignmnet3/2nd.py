#string to tuple
string = "abc"
string_tuple = (string,)
print("String to Tuple : ",string_tuple)

#list to tuple
my_list = [1,2,3,4,5]
list_tuple = tuple(my_list)
print("list to Tuple : ",list_tuple)

#set to tuple
my_set = {1,"apple",109,'grapes'}
set_tuple = tuple(my_set)
print("Set to Tuple : ",set_tuple)

#dictionary to tuple
dict = { 'gazala': 71, 'fadil': 59, 'eshaan': 12, 'ahil': 20 }
dic_tuple = zip(dict.keys(), dict.values())
dic_tuple = tuple(dic_tuple)
print("Dictionary to Tuple :",dic_tuple)
print()