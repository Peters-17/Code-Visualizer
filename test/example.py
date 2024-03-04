class MyClass:
    def method_a(self):
        pass

    def method_b(self):
        self.method_a()

def function_c():
    instance = MyClass()
    instance.method_a()
