# when to store data inside init
# when we need to store the object previous state and when some variable can be used by other function too
# if a function is independent and the variables we not need to hold we store it inside stateless
class Calculator:
    def __init__(self, value_1):
        self.value_1 = value_1


    def add(val_1, val_2):
        return val_1 + val_2

    def sub(val_1, val_2):
        return val_1 - val_2
    def mul(val_1, val_2):
        return val_1*val_2
    def div(val_1, val_2):
        return val_1//val_2
    def mod(val_1, val_2):
        return val_1%val_2

    def sum(self,val_1):
        self.value_1 +=val_1
        return self.value_1
