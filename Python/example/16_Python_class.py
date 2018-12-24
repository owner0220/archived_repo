class Person:
    name="default Name"
    def print(self):
        print("my name is {}".format(self.name))

P1=Person()
P1.print()
P1.name="수정이 되나요??"
P1.print()