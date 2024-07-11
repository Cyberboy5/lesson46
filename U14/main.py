"""
U14:

Car deb nomlangan class yarating. Unda name, price, capacity:int, color, model deb nomlangan atributlar bo'lsin. 
Cardan olingan obyekt print qilinsa avtomobil haqida to'liq ma'lumot ekranga chiqsin.

Carda:
setPrice(),setName(), getPrice(),getName(), setCapacity(),getCapacity(),setColor()
,getColor(), setModel(),getModel() deb nomlangan metodlar bo'lsin.

Address nomnli class yarating. Unda country,city, street nomli  atributlar bo'lsin.
 Addressdan olingan obyekt print qilinsa adressdagi barcha atributlar ekranga chiqsin.

Adressda:
getCountry(),setCountry(),getCity(),setCity(),getStreet().setStreet() nomli metodlar bo'lsin.


CarShowroom nomli class yarating. Unda Adress typida adress, List<Car> typida cars, name, 
rating:List<int>  kabi atributlar bo'lsin.

ushbu classda addCar, removeCar, getCarsInfo, getAdress, changeAdress, changeName, getName, 
rate,getAvarageRating degan metodlar bo'lsin.


- addCar(car:Car)=> car qo'shadi.
- removeCar(car:Car)=>carni o'chiradi
- getCarsInfo()=>Barcha carlarni print qiladi
- getAdress(): Adresni print qiladi
- changeName(newName): Avtasalon nomini almashtiradi
- getName(): Avtasalon nomini print qiladi.
- rate(rate:int): rating qo'shadi(0<n<=5)
- getAvarageRating():o'ratacha ratingni chiqaradi.

Carshowroom obekti print qilinsa, ekranga avtasalon nomi, adresi, nechta avto borligi 
va o'rtacha ratingi ekranga chiqishi kerak.

"""

#code

class Car:
    def __init__(self,name,price,capacity,color,model) -> None:
        self.name = name
        self.price = price
        self.capacity = capacity
        self.color = color
        self.model = model

    def __str__(self) -> str:
        return f"""
    Name:{self.name} 
    Price:{self.price}
    Capacity:{self.capacity}
    Color:{self.color}
    Model:{self.model}
    """

#Price
    def setPrice(self,new_price):
        self.price = new_price

    def getPrice(self):
        return self.price

#Name
    def setName(self,new_Name):
        self.name = new_Name

    def getName(self):
        return self.name
    
#Capacity
    def setCapacity(self,new_capacity):
        self.capacity = new_capacity

    def getCapacity(self):
        return self.capacity

#Color
    def setColor(self,new_color):
        self.color = new_color

    def getColor(self):
        return self.color
    
#Model
    def setModel(self,new_model):
        self.model = new_model

    def getModel(self):
        return self.model
    

class Address:
    def __init__(self,country,city,street) -> None:
        self.country = country
        self.city = city
        self.street = street

    def __str__(self) -> str:
        return f"""
        Counrty:{self.country} 
        City:{self.city}
        Street:{self.street}"""

#Country  
    def setCountry(self,new_country):
        self.country = new_country

    def getCountry(self):
        return self.country

#City
    def setCity(self,new_city):
        self.city = new_city

    def getCity(self):
        return self.city
    
#Street
    def setStreet(self,new_street):
        self.street = new_street

    def getStreet(self):
        return self.street


class CarShowRoom:
    def __init__(self,name,address : Address) -> None:
        self.name = name
        self.address = address
        self.cars = []
        self.rating = []

#Working wiht Cars List
    def addCar(self,new_car):
        if new_car not in self.cars:
            self.cars.append(new_car)
        else:
            raise print("Error:Bu mashina Listda bor")
    
    def removeCar(self,car):
        if car not in self.cars:
            raise print("Car Not Found")
        else:
            self.cars.remove(car)

#Information
    def getCarsInfo(self):
        carsInfo = ""
        for car in self.cars:
            carsInfo += str(car)
        print(carsInfo)

#Address
    def getAddress(self):
        print(self.address)

#Name
    def changeName(self,new_name):
        self.name = new_name
    
    def getName(self):
        print(f"AvtoSalon nomi:'{self.name}'")

#Rating
    def rate(self,rate):

        try:
            if 0 > rate > 5:
                raise print("Rate Is Out Of Range")
            elif 0 <= rate <= 5:
                self.rating.append(rate)

        except Exception as e:
            print(f"Error:{e}")

#Average Rating
    def getAverageRating(self):
        return sum(self.rating) / len(self.rating)
        
        
    def __str__(self) -> str:
        return f"""
    AvtoSalon nomi:{self.name}
    Avtolar soni:{len(self.cars)}
    O`rtacha Reting:{self.getAverageRating()}
    Address:{self.address}
"""
    
# Creating test cases
def test_car_showroom():
    address = Address("Uzbekistan", "Tashkent", "Amir Temur Street")
    showroom = CarShowRoom("UzAuto Motors", address)

    car1 = Car("Chevrolet Spark", 15000, 5, "White", 2023)
    car2 = Car("Chevrolet Malibu", 30000, 5, "Black", 2023)
    car3 = Car("Chevrolet Lacetti", 18000, 5, "Blue", 2022)
    car4 = Car("Chevrolet Captiva", 35000, 7, "Red", 2021)
    car5 = Car("Chevrolet Cobalt", 20000, 5, "Grey", 2023)

    showroom.addCar(car1)
    showroom.addCar(car2)
    showroom.addCar(car3)
    showroom.addCar(car4)
    showroom.addCar(car5)

    # Adding ratings
    showroom.rate(5)
    showroom.rate(4.5)
    showroom.rate(4)
    showroom.rate(3.5)
    showroom.rate(3)

    # Printing car showroom details
    print(showroom)

    # Printing all cars' information
    showroom.getCarsInfo()

    # Removing a car and printing the updated list of cars
    showroom.removeCar(car3)
    showroom.getCarsInfo()

    # Printing the average rating
    print(f"Average Rating: {showroom.getAverageRating()}\n")

# Running the test cases
test_car_showroom()



