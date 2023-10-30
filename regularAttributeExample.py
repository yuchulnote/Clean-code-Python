class ClassWithRegularAttributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter


obj = ClassWithRegularAttributes("some initial value")
print(obj.someAttribute)

obj.someAttribute = "change value"
print(obj.someAttribute)

del obj.someAttribute
print(obj.someAttribute)

"""
some initial value
change value
Traceback (most recent call last):
  File "c:\Users\PETNOW\Desktop\Clean-code-Python\regularAttributeExample.py", line 13, in <module>
    print(obj.someAttribute)
          ^^^^^^^^^^^^^^^^^
AttributeError: 'ClassWithRegularAttributes' object has no attribute 'someAttribute'
"""
