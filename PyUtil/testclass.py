#! /usr/bin/env python3

class TestOne:
    "Description of class"
    name = 'Python class example.'
    def var_type(self, a, b):
        print("Self type => ",type(self))
        print("First var type => ",type(a))
        print("Second var type => ",type(b))
        c = a + b
        print('Sum => ',c)


tone = TestOne()
print(tone)
print(tone.__doc__)
print(tone.name)

try:
    print('try block')
    tone.var_type(2, 10000)
except Exception as e:
    print('catch/except block')
    print(e)
    tone.var_type(10, 49)
else:
    print('No error occured then here.')
finally:
    print('Finally block')