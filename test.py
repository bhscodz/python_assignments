class test:
    class_attr=1
    def __init__(self):
        print(test.class_attr)
        print(self.class_attr)
        test.class_attr+=1

print("obj1")
obj1=test()
print(obj1.__pvt())