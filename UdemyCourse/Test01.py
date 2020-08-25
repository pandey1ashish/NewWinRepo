#! /usr/env/bin python3
"""
print('Normal')
print('-'*20)
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apple', 3))
print('{0:8} | {1:8}'.format('Oranges', 10))
print('{0:8} | {1:8}'.format('Guvava', 5))
print('< Left align')
print('-'*20)
print('{0:8} | {1:<8}'.format('Apple', 3))
print('{0:8} | {1:<8}'.format('Oranges', 10))
print('{0:8} | {1:<8}'.format('Guvava', 5))
print('< Right align')
print('-'*20)
print('{0:8} | {1:>8}'.format('Apple', 3))
print('{0:8} | {1:>8}'.format('Oranges', 10))
print('{0:8} | {1:>8}'.format('Guvava', 5))
print('< Center align')
print('-'*20)
print('{0:8} | {1:^8}'.format('Apple', 3))
print('{0:8} | {1:^8}'.format('Oranges', 10))
print('{0:8} | {1:^8}'.format('Guvava', 5))
"""

"""
fruit = input('Provide fruit name: ')
print('I love {}, as informed.'.format(fruit))
"""

"""
intvar = 123
fltvar = 2.5

print(intvar)
print(type(intvar))

print(fltvar)
print(type(fltvar))
"""

"""
def say_hi(name = 'there'):
    print('Hi {}!'.format(name))

say_hi()
say_hi('Ashish')
"""


contacts = {'Ashish': '8056762918', 'Mamta': '8173058500'}
ashish_contact = contacts['Ashish']
mamta_contact = contacts['Mamta']

print(len(contacts))
print('Dial {} to contact Ashish.'.format(ashish_contact))
print('Dial {} to contact Mamta.'.format(mamta_contact))

print('8056762918' in contacts.values())