"""
U17:

Qo`shimcha Misol

"""

#code

class MyDate:
    def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year
        self.MONTHS = ["January","February","March","April", "May","June", "July","August", 
                        "September", 
                        "October",
                        "November",
                        "December"
                        ]
        self.DAY_IN_MONTHS = [31,29,31,30,31,30,31,31,30,31,30,31]

#IsValid
    def isLeapYear(self):
        if isinstance(self,MyDate):
            if self.__year % 4 == 0 and self.__year % 100 != 0 and not self.__year % 400 == 0:
                return True
        return False
        
    def isValidDate(self):
        if not self.isLeapYear() and self.__month == 2 and self.__day == 29:
            return False
        elif (1 <= self.__year <= 9999) and ( 1<= self.__month <= 12) and (1 <= self.__day <= 31):
            return True
        return False

#SETTERS
    def setDate(self,day,month,year):
        if  self.isValidDate(day,month,year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            print("Invalid year,day or month")

    def setYear(self,new_year):
        if (1 <= new_year >= 9999):
            self.__year = new_year
        else:
            print("Invalid Year")

    def setMonth(self,new_month):
        if (1 <= new_month >= 31):
            self.__month = new_month
        else:
            print("Invalid month")
                        
    def setDay(self,new_day : int):
        if (1 <= new_day >= 31):
            self.__day = new_day
        else:
            print("Invalid Day")

#GWTTERS
    def getYear(self):
        return f"Year:{self.__year}"
    
    def getMonth(self):
        return f"Month:{self.__month}"

    def getDay(self):
        return f"Day:{self.__day}"

    def __repr__(self):
        return f"{self.__day}-{self.MONTHS[self.__month-1]} {self.__year} yil"


#Next and Previous MyDate
#Next
    def nextDay(self):
        if self.isLeapYear() and self.__month == 2 and self.__day == 29:
            self.__month += 1
            self.__day = 1
        else:
            if self.__day == self.DAY_IN_MONTHS[self.__month-1]:
                self.__day = 1
                if self.__month == 12:
                    self.__month = 1
                    self.__year += 1
                else:
                    self.__month +=1
            else:
                self.__day += 1
                
        return self
    

    def nextMonth(self):        
        if self.__month == 12:
            self.__month = 1
            self.__year += 1
        else:
            self.__month +=1
        self.__day = 1

        return self

    def nextYear(self):
        try:
            self.__year += 1
            if 1 <= self.__year <= 9999:
                return self
            else:
                raise print("Year Is Out Of Range") 
            
        except Exception as e:
            print(f"Error: {e}")

#Prevoius
    def previousDay(self):
        if self.__day == 1:
            self.__day = self.DAY_IN_MONTHS[self.__month-1]
            if self.__month == 1:
                self.__month = 12
                self.__year -= 1 
            else:
                self.__month -=1
        else:
            self.__day -= 1 

        return self

    def previousMonth(self):
        if self.__month == 1:
            self.__month = 12
            self.__year -=1
        else:
            self.__month -=1
        self.__day = self.DAY_IN_MONTHS[self.__month-1]

        return self
        
    def previousYear(self):
        try:
            if self.isLeapYear() and self.__month == 2 and self.__day == 29:
                self.__day = 28
                self.__year -=1
                return self

            else:
                self.__year -= 1
                if 1 <= self.__year <= 9999:
                    return self
                else:
                    raise print("Year Is Out Of Range") 
            
        except Exception as e:
            print(f"Error: {e}")



#CASES

print()

d1 = MyDate(28,2,2012)
# print(d1)
# print(d1.nextDay())
# print(d1.nextDay())
# print(d1.nextMonth())           
# print(d1.nextYear())


d2 = MyDate(2,1,2012)
# print(d2)
# print(d2.previousDay())
# print(d2.previousDay())
# print(d2.previousMonth())
# print(d2.previousYear())


d3 = MyDate(29,2,2012)
# print(d3.previousYear())


#Shuni Case da xatolik bor ekan bu d4 date aslida True bo`lishi kerak ,u caseda False beribdi
d4 = MyDate(31,11,2099)
print(d4.isValidDate())


d5 = MyDate(29,2,2011)
# print(d5.isValidDate())
print()