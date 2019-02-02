class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
        
    def rot(self, days, temp):
        self.mold = days * temp
        
or1 = Orange(4, "light orange")
        
orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

