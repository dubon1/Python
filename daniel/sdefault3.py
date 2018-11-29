#!/usr/bin/python3 

import collections 
import itertools 

my_list_dict = [
    {'model': u'Yaris', 'some_value': 11202, 'trim_name': u'3-Door L Manual'},
    {'model': u'Yaris', 'some_value': 19269, 'trim_name': u'3-Door LE Automatic'},
    {'model': u'Corolla', 'some_value': 27119, 'trim_name': u'L Automatic'},
    {'model': u'Corolla', 'some_value': 32262, 'trim_name': u'LE'},
    {'model': u'Corolla', 'some_value': 37976, 'trim_name': u'S Premium'},
    {'model': u'Camry', 'some_value': 39730, 'trim_name': u'LE 4-Cyl'},
    {'model': u'Camry', 'some_value': 45761, 'trim_name': u'XSE 4-Cyl'},
    {'model': u'Yaris', 'some_value': 48412, 'trim_name': u'3-Door L Automatic'},
    {'model': u'Camry', 'some_value': 55423, 'trim_name': u'XLE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 57055, 'trim_name': u'ECO Premium'},
    {'model': u'Corolla', 'some_value': 61296, 'trim_name': u'ECO Plus'},
    {'model': u'Camry', 'some_value': 63660, 'trim_name': u'XSE V6'},
    {'model': u'Yaris', 'some_value': 65570, 'trim_name': u'5-Door LE Automatic'},
    {'model': u'Camry', 'some_value': 67461, 'trim_name': u'XLE V6'},
    {'model': u'Corolla', 'some_value': 73602, 'trim_name': u'S'},
    {'model': u'Yaris', 'some_value': 74158, 'trim_name': u'5-Door SE Manual'},
    {'model': u'Corolla', 'some_value': 74249, 'trim_name': u'LE Plus'},
    {'model': u'Corolla', 'some_value': 78386, 'trim_name': u'ECO'},
    {'model': u'Camry', 'some_value': 82747, 'trim_name': u'SE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 83162, 'trim_name': u'LE Premium'},
    {'model': u'Corolla', 'some_value': 84863, 'trim_name': u'S Plus Manual'},
    {'model': u'Yaris', 'some_value': 90313, 'trim_name': u'5-Door L Automatic'},
    {'model': u'Corolla', 'some_value': 90452, 'trim_name': u'L Manual'},
    {'model': u'Yaris', 'some_value': 93152, 'trim_name': u'5-Door SE Automatic'},
    {'model': u'Corolla', 'some_value': 94973, 'trim_name': u'S Plus CVT'},
]

# method 1
new_dict=collections.defaultdict(list)
for each_dict_row in my_list_dict:
    # each dict row has multiple VALUES
    new_dict[each_dict_row['model']].append(each_dict_row) 

# million $ Q to split at will    mission impossible
for each_model, the_rest in new_dict.items():
    print('\n\n\n\n')
    print(each_model)
    print(the_rest, '\n') 

print('\n\n\n\n\n\n\n\n')

# method 2
def keyfunc(x): 
    return x['model']

my_list_dict=sorted(my_list_dict, key=keyfunc)
for model, group in itertools.groupby(my_list_dict, keyfunc):
  print() 
  print(model) 

  
# print(list(group))
# for k, v in list(group).iteritems():
#   print(k, '    value : ', v)





