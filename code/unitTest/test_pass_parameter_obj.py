class Number:
    def __init__(self):
        self.a = 0

    def add_one(self):
        self.a += 1

class Other:
    def __init__(self, obj_test):
        self.__object_test = obj_test

    def print_value(self):
        name = list({var_name : var_obj for var_name, var_obj in locals().items() if var_obj == self}.keys())[0]
        print(f"\t{name}: {self.__object_test.a}")

    def add_one(self):
        self.__object_test.add_one()

if __name__ == '__main__':
    num = Number()
    other1 = Other(num)
    other1.add_one()
    other1.print_value()
    other2 = Other(num)
    other2.add_one()
    other2.print_value()


