class A:
    none_changing_list = []
    def __init__(self) -> None:
        self.changing_list = []
obj1 = A()
obj2 = A()
obj1.changing_list.append("test")
obj1.none_changing_list.append("test2")
print(obj2.none_changing_list)