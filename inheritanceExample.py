class ParentClass:
    def printHello(self):
        print("Hello, world!")


class ChildClass(ParentClass):
    def someNewMethod(self):
        print("ParentClass objects don't have this method.")  # 클린 코드 책 오타


class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print("Only GrandchildClass objects have this method.")


print("Create ParentClass object and call its method:")
parent = ParentClass()
parent.printHello()


print("Create ChildCalss object and call its methods:")
child = ChildClass()
child.printHello()
child.someNewMethod()


print("Create GrandchildCalss object and call its methods:")
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMethod()
grandchild.anotherNewMethod()


print("An error:")
parent.someNewMethod()
