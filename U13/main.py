"""
U13:

Shape nomli Perent class berilgan va uning 4ta child classi bor.

1-class Line(chiziq), 
2-class Triangle(Uchburchak), 
3-class Rectangle(To'rtburchak)
4-class NullShape(bo'sh shakl). 
symbol va lenght propertysi bor.

Ularda show(), setSymbol(), setLength() degan metod bor.

Input:

L = Line(8)   
L.show()   

Output:

* * * * * * * *

Input:
T = Triangle()
T.show()

Output:
*
* *
* * *
* * * *
* * * * *

Input:
R = Rectangle(4)
R.setLength(6)
R.show()

Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

Input:
S = NullShape(10)
S.show()

Output:
"Bo'sh shakl" degan yozuvchiqsin.

"""

#code

class Shape:
    def __init__(self,lenth = 5,symboy = "*",) -> None:
        self.symbol = symboy
        self.lenth = lenth

    def setSymbol(self,new_symbol):
        self.symbol = new_symbol

    def setLenth(self,new_lenth):
        self.lenth = new_lenth


class Line(Shape):
    def __init__(self,lenth = 5, symboy = "*") -> None:
        super().__init__(lenth,symboy)

    def show(self):
        print(self.symbol*self.lenth)


class Triangle(Shape):
    def __init__(self,lenth = 5, symboy = "*") -> None:
        super().__init__(lenth,symboy)

    def show(self):
        for i in range(1,self.lenth+1):
            print(self.symbol*i)


class Rectangle(Shape):

    def __init__(self, lenth = 5, symboy = "*") -> None:
        super().__init__(lenth, symboy)


    def show(self):
        for _ in range(self.lenth):
            print(self.symbol*self.lenth)


class NullShape(Shape):
    
    def __init__(self, lenth = None, symboy = None) -> None:
        super().__init__(lenth, symboy)

    def show(self):
        print("Bo'sh shakl")


# L = Line()   
# L.show()   

# T = Triangle()
# T.show()

# R = Rectangle(4)
# R.setLenth(6)
# R.show()

# S = NullShape()
# S.show()

