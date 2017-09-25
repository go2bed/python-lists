my_dict = {'key': 'value', 'key2': 'value2'}
print(my_dict['key'])
my_dict = {'k1': 123, 'k2': 3.14, 'k3': 'string'}
print(my_dict['k3'])
print(my_dict['k3'][::-1])
print(my_dict['k3'].upper())
print(my_dict['k1'])
my_dict['k1'] = my_dict['k1'] - 120
print(my_dict['k1'])
my_dict['k1'] += 100
print(my_dict['k1'])
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print(d)
d = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(d['k1'])
print(d['k1']['nestkey'])
print(d['k1']['nestkey']['subnestkey'].upper())
