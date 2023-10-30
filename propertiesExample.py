class ClassWithProperties:
    def __init__(self):
        self.someAttribute = "some initial value"

    @property
    def someAttribute(self):  # 이것은 "getter" 메소드다
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value):  # 이것은 "setter" 메소드다
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self):  # 이것은 "deleter" 메소드다
        del self._someAttribute


obj = ClassWithProperties()
print(obj.someAttribute)

obj.someAttribute = "change value"
print(obj.someAttribute)

del obj.someAttribute
