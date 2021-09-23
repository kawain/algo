class ClassA:
    obj = None
    num = 0

    @staticmethod
    def get_instance():
        if ClassA.obj is None:
            ClassA.obj = ClassA()
            return ClassA.obj
        else:
            return ClassA.obj

    def msg(self):
        ClassA.num += 1
        print(ClassA.num)

    # 初めてのときだけobjに代入
    # 2回目以降エラー
    def __init__(self):
        if ClassA.obj is not None:
            raise Exception("Singletonクラス")
        else:
            ClassA.obj = self


o3 = ClassA()
o3.msg()
print(id(o3))

o1 = ClassA.get_instance()
o1.msg()
print(id(o1))

o2 = ClassA.get_instance()
o2.msg()
print(id(o2))
