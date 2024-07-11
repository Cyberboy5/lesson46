"""
4-masala. PROGRAMMER
Developer nomli class yarating va uning property elementlari quyidagilardan iborat:

Surname(Familiyasi);
Position(Lavozimi);
Salary(Oyligi).
SoftwareEngineer nomli class Developer classidan voris bo`lib keladi va uning property elementlari quyidagilardan iborat:

Surname(Familiyasi);
Position(Lavozimi);
Salary(Oyligi);
Bonus(Oyligiga qo`shib beriladigan ustama haqi);
Department(Bo`lim nomi).
SoftwareEngineer nomli classning 5ta obyektini yarating. Sizning vazifangiz ushbu obyektlar orasidagi
 dasturchilarining har bir bo`limi uchun ustama haqi bilan birga qancha summa to`langanligini aniqlang.

Eslatma: Barcha ma`lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo`yiladi.

Input (Kiruvchi ma'lumot)


Anvar Junior 500 100 1-bo'lim
Asror Middle 1500 500 2-bo'lim
Kamola Senior 2500 1000 3-bo'lim
Vali Junior 500 -100 1-bo'lim
Davron Middle 1500 100 2-bo'lim
Farrux Junior 500 -100 1-bo'lim
Sherzod Middle 1500 200 2-bo'lim
Jasur Senior 2500 1000 3-bo'lim
Jamila Junior 500 -100 1-bo'lim
Output (Chiquvchi ma'lumot)

Output:
1-bo'lim 2000
2-bo'lim 5300
3-bo'lim 7800

"""

#code

class Developer:
    def __init__(self,surname,position,salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary


class SoftwareEngineer(Developer):
    def __init__(self, surname, position, salary,bonus,department) -> None:
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department

#MAIN
engineers = [
    SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Asror", "Middle", 1500, 500, "2-bo'lim"),
    SoftwareEngineer("Kamola", "Senior", 2500, -100, "3-bo'lim"),
    SoftwareEngineer("Vali", "Junior", 500, -100, "1-bo'lim"),
    SoftwareEngineer("Davron", "Middle", 1500, 100, "2-bo'lim"),
    SoftwareEngineer("Bahodir", "Senior", 2500, -100, "3-bo'lim"),
    SoftwareEngineer("Farrux", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Jamila", "Middle", 1500, 200, "2-bo'lim"),
    SoftwareEngineer("Jasur", "Senior", 2500, 500, "3-bo'lim"),
    SoftwareEngineer("Komila", "Junior", 500, -100, "1-bo'lim")
    ]


departments = {}
for engineer in engineers:
    if engineer.department not in departments:
        departments[engineer.department] = 0
    departments[engineer.department] += engineer.salary + engineer.bonus

# Displaying results
print()
for department, total_salary in departments.items():
    print(f"{department} {total_salary}")
print()