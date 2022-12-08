

class MyClass(object):
    classy = "This is a classy attribute"
    def set_value(self):
        self.insty = "This is a insty attribute"

obj = MyClass()
obj.set_value()
print(obj.insty)