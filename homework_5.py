my_list=['KIA', 'TOYOTA', 'MERSEDES', 'BMW', 'LADA']
print(my_list)
print(my_list[::len(my_list)-1])
print(my_list[2:5])
my_list[2]= 'AUDI'
print(my_list)

my_dict={'собака': 'dog',
         'кошка' : 'cat',
         'лиса': 'fox',
         'медведь': 'bear'}
print(my_dict)
print(my_dict['лиса'])
my_dict['лиса']= 'wolf'
my_dict['мышь']= 'mouse'
print(my_dict)